from django.urls import path
from .views import (
    AboutView, CustomerView, CatalogConstructionView, 
    CatalogFoodView, ContactView, HomeView, SellerDetailView, SellerView, CustomerDetailView,
    ProductTextView, HowToByView, export_excelView, simple_upload
)

urlpatterns = [ 
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('customers/', CustomerView.as_view(), name='customers'),
    path('customers/<int:pk>/',CustomerDetailView.as_view(), name='customer_detail'),
    path('sellers/', SellerView.as_view(), name='sellers'),
    path('sellers/<int:pk>/', SellerDetailView.as_view(), name='seller_detail'),
    path('catalog/', CatalogConstructionView.as_view(), name='catalog-construction'),
    path('catalog-food/', CatalogFoodView.as_view(), name='catalog_food'),
    path('product-text/', ProductTextView.as_view(), name='product_text'),
    path('how-to-by/',HowToByView.as_view(), name='how-to-by'),
    path('contact/', ContactView.as_view(), name='contact'),

    path('export-excel/', export_excelView, name='export-excel'),

    path('upload-excel/', simple_upload, name='excel-upload'),



]