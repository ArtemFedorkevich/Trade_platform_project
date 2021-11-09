from Items.models import Inventory

from Items.serializers import InventorySerializer

from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets, mixins


#Class for creation of Inventories
class InventoryViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Endpoint for creation of user inventory
    """
    permission_classes = IsAuthenticated,
    serializer_class = InventorySerializer

    def get_queryset(self):
        queryset = Inventory.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)