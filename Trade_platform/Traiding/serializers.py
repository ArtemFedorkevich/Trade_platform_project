from rest_framework import serializers

from Traiding.models import Offer


class OfferSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Offer
        fields = ('id', 'entry_quantity', 'order_type', 'price', 'is_active', 'item', 'user')
