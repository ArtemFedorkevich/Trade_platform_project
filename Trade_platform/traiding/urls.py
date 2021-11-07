from Items.urls import router

# This routher add paths to routher form authentication.urls
from traiding import views

router.register(r'offer', views.OfferViewSet, basename="offer_creation")

urlpatterns = router.urls
app_name = 'traiding'