from django.urls import path
from .views import (
    AboutView, BuyerView, CatalogConstructionView, 
    CatalogFoodView, ContactView, HomeView, ManufacturerView, 
    ProductTextView, HowToByView,BuyerDetailView
)

urlpatterns = [ 
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('manufacturers/', ManufacturerView.as_view(), name='manufacturer'),
    path('buyers/', BuyerView.as_view(), name='buyer'),
    path('buyers/<int:pk>/', BuyerDetailView.as_view()),
    path('catalog-construction/', CatalogConstructionView.as_view(), name='catalog-construction'),
    path('catalog-food/', CatalogFoodView.as_view(), name='catalog_food'),
    path('product-text/', ProductTextView.as_view(), name='product_text'),
    path('how-to-by/',HowToByView.as_view(), name='how-to-by'),
    path('contact/', ContactView.as_view(), name='contact'),



]