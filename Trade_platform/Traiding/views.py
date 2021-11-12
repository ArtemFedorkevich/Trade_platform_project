from Traiding.models import Offer

from Traiding.serializers import OfferSerializer

from Items.models import Item, Inventory

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

from rest_framework import viewsets, mixins, status

class OfferViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Endpoint for creation of offer information
    """
    permission_classes = IsAuthenticated,
    serializer_class = OfferSerializer


    def get_queryset(self):
        queryset = Offer.objects.filter(user=self.request.user)
        return queryset


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(serializer)
        item = Item.objects.get(pk=request.data['item'])

        #Quantity of stocks that user have
        user_stock = Inventory.objects.get(user=request.user, item=request.data['item'])

        #Quantity of stocks in offers
        alloffer_stock = Offer.objects.filter(user=request.user, item=request.data['item'], order_type=2).values_list('entry_quantity', flat=True)

        #Check that amount stocks in inventory is higher than quantity in table offer for selling plus input value
        #You can't sell more stocks than you have
        if user_stock.quantity < sum(alloffer_stock)+request.data['entry_quantity'] and request.data['order_type'] == 2:
            raise ValueError('You have not enough stocks. Input smaller value')
        else:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer, request, item)
            headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer, request, item):
        serializer.save(user=self.request.user, item=item)
