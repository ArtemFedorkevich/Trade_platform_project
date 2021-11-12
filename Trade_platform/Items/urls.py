from rest_framework.routers import DefaultRouter

# This router add paths to router form authentication.urls
from Items.views import Currencyview, Itemview, Inventoryview, Watchlistview, Moneyview


router = DefaultRouter()
router.register(r'currency', Currencyview.CurrencyViewSet, basename="currency_creation")
router.register(r'item', Itemview.ItemsViewSet, basename="item_creation")
router.register(r'inventory', Inventoryview.InventoryViewSet, basename="inventory_creation")
router.register(r'watch_list', Watchlistview.WatchListViewSet, basename="watch_list_creation")
router.register(r'money', Moneyview.MoneyViewSet, basename="money_adding")
