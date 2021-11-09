from rest_framework import serializers

from Items.models import Currency, Item, Inventory, WatchList, Money


# This is the serializer for adding of currency by admin(is_staff = 1 in database)
class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = ('id', 'code', 'name')


# This is the serializer for adding of items by admin(is_staff = 1 in database)
class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('id', 'code', 'name', 'price', 'currency')


# This is the serializer for adding of items by admin(is_staff = 1 in database)
class InventorySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Inventory
        fields = ('id', 'user', 'item', 'quantity')


# This is the serializer for adding of items by admin(is_staff = 1 in database)
class WatchListSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = WatchList
        fields = ('id', 'user', 'item', )



#This serializer for get-request watchlist endpoint
class GetWatchListSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = WatchList
        fields = ('id', 'user', 'item')


#This serializer for adding money
class MoneySerializer(serializers.ModelSerializer):

    class Meta:
        model = Money
        fields = ('id', 'user', 'money', )
