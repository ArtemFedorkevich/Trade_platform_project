from Items.urls import router

# This routher add paths to routher form authentication.urls
from Traiding import views

router.register(r'offer', views.OfferViewSet, basename="offer_creation")
app_name = 'Traiding'