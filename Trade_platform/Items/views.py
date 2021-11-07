from Items.models import Currency, Item, Inventory, WatchList, Money

from Items.serializers import (
    CurrencySerializer, ItemSerializer, InventorySerializer, WatchListSerializer, GetWatchListSerializer, MoneySerializer
    )

from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated

from rest_framework.response import Response

from rest_framework import viewsets, mixins, status

#Class for creation of currency
class CurrencyViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Endpoint for creation of currency information
    """
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

    # All authenticated users can see currency, only staff can create currency.
    def get_permissions(self):
        if self.request.method in ('POST'):
            self.permission_classes = (IsAdminUser,)
        else:
            self.permission_classes = (IsAuthenticated,)

        return super().get_permissions()

    # Staff (is_staff = 1 in database) can add currency.
    def get(self, request, *args, **kwargs):
        """
        This will return list of curencies.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        This will create a currency.
        """
        return self.create(request, *args, **kwargs)

#Class for creation of Items
class ItemsViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    # All authenticated users can see items, only staff can create items.
    def get_permissions(self):
        if self.request.method in ('POST'):
            self.permission_classes = (IsAdminUser,)
        else:
            self.permission_classes = (IsAuthenticated,)

        return super().get_permissions()

    def get(self, request, *args, **kwargs):
        """
        This will return list of items.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        This will create a item.
        """
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        currency = Currency.objects.get(pk=request.data['currency'])
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, currency)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer, currency):
        serializer.save(currency=currency)


#Class for creation of Inventories
class InventoryViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Inventory.objects.all()
    permission_classes = IsAuthenticated,
    serializer_class = InventorySerializer

    def get(self, request, *args, **kwargs):
        """
        This will return list of inventories.
        """
        return self.list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = Inventory.objects.filter(user=request.user)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """
        This will create a invetory.
        """
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        item = Item.objects.get(pk=request.data['item'])
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, request, item)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer, request, item):
        serializer.save(user=self.request.user, item=item)

class WatchListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = WatchList.objects.all()
    permission_classes = IsAuthenticated,
    serializer_class = WatchListSerializer

    # change to IsAdminUser in the last version
    def get(self, request, *args, **kwargs):
        """
        This will return list of favorite stocks.
        """
        return self.list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = WatchList.objects.filter(user=request.user)
        serializer = GetWatchListSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """
        This will create a favorite stock.
        """
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        item = Item.objects.get(pk=request.data['item'])
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, request, item)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer, request, item):
        serializer.save(user=self.request.user, item=item)

class MoneyViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Money.objects.all()
    permission_classes = IsAuthenticated,
    serializer_class = MoneySerializer

    def get(self, request, *args, **kwargs):
        """
        This will return value of user money.
        """
        return self.list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = Money.objects.filter(user=request.user)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """
        This will create a user money.
        """
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, request)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer, request):
        serializer.save(user=self.request.user)