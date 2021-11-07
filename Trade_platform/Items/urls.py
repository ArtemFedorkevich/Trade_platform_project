from authentication.urls import router

# This routher add paths to routher form authentication.urls
from Items import views

router.register(r'currency', views.CurrencyViewSet, basename="currency_creation")
router.register(r'item', views.ItemsViewSet, basename="item_creation")
router.register(r'inventory', views.InventoryViewSet, basename="inventory_creation")
router.register(r'watch_list', views.WatchListViewSet, basename="watch_list_creation")
router.register(r'money', views.MoneyViewSet, basename="money_adding")
urlpatterns = router.urls
app_name = 'Items'