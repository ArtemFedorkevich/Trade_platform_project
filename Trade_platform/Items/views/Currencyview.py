from Items.models import Currency

from Items.serializers import CurrencySerializer

from rest_framework.permissions import IsAdminUser, IsAuthenticated

from rest_framework import viewsets, mixins


# Class for creation of currency
class CurrencyViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Endpoint for creation of currency information
    """
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

    # All authenticated users can see currency, only staff can create currency.
    def get_permissions(self):
        if self.request.method in ('POST',):
            self.permission_classes = (IsAdminUser, IsAuthenticated,)
        else:
            self.permission_classes = (IsAuthenticated,)
        return super().get_permissions()
