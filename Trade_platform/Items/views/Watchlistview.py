from Items.models import WatchList

from Items.serializers import WatchListSerializer, GetWatchListSerializer

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

from rest_framework import viewsets, mixins


# ViewSet for creation watchlist
class WatchListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Endpoint for creation of user watchlist
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = WatchListSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)

    # Use GetWatchlistSerializer to show information about item (code, name) for get request
    def list(self, request, *args, **kwargs):
        queryset = WatchList.objects.filter(user=self.request.user)
        serializer = GetWatchListSerializer(queryset, many=True)
        return Response(serializer.data)
