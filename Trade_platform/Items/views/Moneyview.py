from Items.models import Money

from Items.serializers import MoneySerializer

from rest_framework.permissions import IsAdminUser, IsAuthenticated

from rest_framework import viewsets, mixins


# ViewSet for adding money for user
class MoneyViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Endpoint for adding of information about user money
    """
    serializer_class = MoneySerializer

    def get_permissions(self):
        if self.request.method in ('POST',):
            self.permission_classes = (IsAdminUser, IsAuthenticated)
        else:
            self.permission_classes = (IsAuthenticated,)
        return super().get_permissions()

    def get_queryset(self):
        queryset = Money.objects.filter(user=self.request.user)
        return queryset
