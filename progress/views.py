from progress.models import HomeImage, Logistic,Product, Category, Certificate, Gallery, Customer, Seller
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView


class HomeView(ListView):
    queryset = HomeImage.objects.all()
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()[:8]
        context['popular_products'] = Product.objects.filter(type='POP')[:8]
        return context
  


class AboutView(ListView):
    queryset = Gallery.objects.all()
    template_name = 'about.html'
    context_object_name = 'galeries'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['certificates'] = Certificate.objects.all()[:8]
        return context


class CustomerView(ListView):
    queryset = Customer.objects.all()[:8]
    template_name = 'customers.html'
    context_object_name = 'customers'

class CustomerDetailView(DetailView):
    queryset = Customer.objects.all()
    template_name = 'customer_detail.html'
    context_object_name = 'customer'



class SellerView(ListView):
    queryset = Seller.objects.all()[:8]
    template_name = 'sellers.html'
    context_object_name = 'sellers'

class SellerDetailView(DetailView):
    queryset = Seller.objects.all()
    template_name = 'seller_detail.html'
    context_object_name = 'seller'




class CatalogConstructionView(ListView):
    queryset = Product.objects.all()
    template_name = 'catalog_construction.html'
    context_object_name = 'products'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(parent__name='Строительный')
        context['sellers'] = Seller.objects.all()
        context['new_products'] = Product.objects.filter(type='NEW')
        cat_id = self.request.GET.get('category',None)
        print(cat_id)
        if cat_id:
            products = Product.objects.filter(category=cat_id)
            context['products']  = products   
            print(products)
        else:
            products = Product.objects.filter(category__parent__name='Строительный')
            context['products']  = products
        return context

class CatalogFoodView(ListView):
    queryset = queryset = Product.objects.all()
    template_name = 'catalog_food.html'
    context_object_name = 'products'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(parent__name='Продукты')
        context['sellers'] = Seller.objects.all()
        context['new_products'] = Product.objects.filter(type='NEW')
        cat_id = self.request.GET.get('category',None)
        if cat_id:
            products = Product.objects.filter(category=cat_id)
            context['products']  = products  
        else:
            products = Product.objects.filter(category__parent__name='Продукты')
            context['products']  = products 
        return context
    

class ProductTextView(ListView):
    queryset = queryset = Product.objects.all()
    template_name = 'catalog_text.html'
    context_object_name = 'products'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(parent__name = 'Текстильные')
        context['sellers'] = Seller.objects.all()
        context['new_products'] = Product.objects.filter(type='NEW')
        cat_id = self.request.GET.get('category',None)
        if cat_id:
            products = Product.objects.filter(category=cat_id)
            context['products']  = products 
        else:
            products = Product.objects.filter(category__parent__name='Текстильные')
            context['products']  = products   
        return context
    

class HowToByView(ListView):
    queryset = Logistic.objects.all()
    template_name = 'logistics.html'
    context_object_name = 'logistics'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logistics_price'] = self.queryset.filter(place_name=self.request.POST.get('city',None)).first()
        print(context['logistics'])
        return context

class ContactView(TemplateView):
    template_name ='contact.html'
