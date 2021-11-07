from traiding.models import Offer

from traiding.serializers import OfferSerializer

from Items.models import Item, Inventory

from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated

from rest_framework.response import Response

from rest_framework import viewsets, mixins, status

class OfferViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Endpoint for creation of offer information
    """
    queryset = Offer.objects.all()
    permission_classes = IsAuthenticated,      #change to IsAdminUser in the last version
    serializer_class = OfferSerializer

    # Staff (is_staff = 1 in database) can add currency.
    def get(self, request, *args, **kwargs):
        """
        This will return list of offers.
        """
        return self.list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = Offer.objects.filter(user=request.user)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """
        This will create a offer.
        """
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        item = Item.objects.get(pk=request.data['item'])

        #Quantity of stocks that user have
        user_stock = Inventory.objects.get(user=request.user, item=request.data['item'])

        #Quantity of stocks in offers
        alloffer_stock = Offer.objects.filter(user=request.user, item=request.data['item']).values_list('entry_quantity', flat=True)

        #Check that amount stocks in inventory is higher than quantity in offer plus input value
        if user_stock.quantity < sum(alloffer_stock)+request.data['entry_quantity']:
            raise ValueError('You have not enough stocks. Input smaller value')
        else:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer, request, item)
            headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer, request, item):
        serializer.save(user=self.request.user, item=item)
