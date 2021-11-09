from Items.models import Item

from Items.serializers import ItemSerializer

from rest_framework.permissions import IsAdminUser, IsAuthenticated

from rest_framework import viewsets, mixins


#Class for creation of Items
class ItemsViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Endpoint for creation of items by admin
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    # All authenticated users can see items, only staff can create items.
    def get_permissions(self):
        if self.request.method in ('POST'):
            self.permission_classes = (IsAdminUser, IsAuthenticated)
        else:
            self.permission_classes = (IsAuthenticated,)
        return super().get_permissions()

