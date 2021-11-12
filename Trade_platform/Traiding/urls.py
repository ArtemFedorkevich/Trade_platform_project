from Items.urls import router

from Traiding import views

router.register(r'offer', views.OfferViewSet, basename="offer_creation")
app_name = 'Traiding'
