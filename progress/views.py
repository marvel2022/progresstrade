import imp

from django.shortcuts import render
from django.views.generic import TemplateView, DetailView


class HomeView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'

class ManufacturerView(TemplateView):
    template_name = 'manufacturers.html'

class BuyerView(TemplateView):
    template_name = 'buyers.html'

class BuyerDetailView(DetailView):
    template_name = 'buyers-detail.html'



class CatalogConstructionView(TemplateView):
    template_name = 'catalog_construction.html'

class CatalogFoodView(TemplateView):
    template_name = 'catalog_food.html'

class ProductTextView(TemplateView):
    template_name = 'product_textile.html'

class HowToByView(TemplateView):
    template_name = 'how_to_by.html'

class ContactView(TemplateView):
    template_name ='contact.html'
