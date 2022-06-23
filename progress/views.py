from itertools import product
from unicodedata import category
from urllib import response

from django.http import HttpResponse
from progress.models import HomeImage, Logistic,Product, Category, Certificate, Gallery, Customer, Seller
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
import xlwt
from datetime import datetime

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
    context_object_name = 'products1'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(parent__name='Строительный')
        if self.request.GET.get('seller', None) and self.request.GET.get('category',None):
            context['products'] = Product.objects.filter(seller=self.request.GET.get('seller'),category=self.request.GET.get('category',None))
            print(f"Products ------->  {Product.objects.filter(seller=self.request.GET.get('seller'),category=self.request.GET.get('category',None))}")
            context['categories'] = Category.objects.filter(products__seller=self.request.GET.get('seller', None))
            context['sellers'] = Seller.objects.all()
        elif self.request.GET.get('seller', None):
            print(self.request.GET.get('seller', None))
            context['sellers'] = Seller.objects.all()
            context['products'] = Product.objects.filter(seller=self.request.GET.get('seller', None))
            print(F"products -------> {context['products']}")
            context['categories'] = Category.objects.filter(products__seller=self.request.GET.get('seller', None))
            context['seller_id']=  Seller.objects.filter(id=self.request.GET.get('seller', None)).first().id
       
        elif self.request.GET.get('category',None):
            context['products'] = Product.objects.filter(category=self.request.GET.get('category',None))
            print(context['products'])
            context['categories'] = Category.objects.filter(parent__name='Строительный')
            context['sellers'] = Seller.objects.filter(products__category__id=self.request.GET.get('category',None))
        else:
            context['categories'] = Category.objects.filter(parent__name='Строительный')
            context['sellers'] = Seller.objects.all()
            context['products'] = Product.objects.all()

        
        context['new_products'] = Product.objects.filter(type='NEW')
        # cat_id = self.request.GET.get('category',None)
        # print(cat_id)
        # print(self.requets.path)
        # if cat_id:
        #     products = Product.objects.filter(category=cat_id)
        #     context['products']  = products   
        #     print(products)
        # else:
        #     products = Product.objects.filter(category__parent__name='Строительный')
        #     context['products']  = products
        return context

class CatalogFoodView(ListView):
    queryset = queryset = Product.objects.all()
    template_name = 'catalog_food.html'
    context_object_name = 'products'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(parent__name='Строительный')
        if self.request.GET.get('seller', None) and self.request.GET.get('category',None):
            context['products'] = Product.objects.filter(seller=self.request.GET.get('seller'),category=self.request.GET.get('category',None))
            print(f"Products ------->  {Product.objects.filter(seller=self.request.GET.get('seller'),category=self.request.GET.get('category',None))}")
            context['categories'] = Category.objects.filter(products__seller=self.request.GET.get('seller', None))
            context['sellers'] = Seller.objects.all()
        elif self.request.GET.get('seller', None):
            print(self.request.GET.get('seller', None))
            context['sellers'] = Seller.objects.all()
            context['products'] = Product.objects.filter(seller=self.request.GET.get('seller', None))
            print(F"products -------> {context['products']}")
            context['categories'] = Category.objects.filter(products__seller=self.request.GET.get('seller', None))
            context['seller_id']=  Seller.objects.filter(id=self.request.GET.get('seller', None)).first().id
       
        elif self.request.GET.get('category',None):
            context['products'] = Product.objects.filter(category=self.request.GET.get('category',None))
            print(context['products'])
            context['categories'] = Category.objects.filter(parent__name='Строительный')
            context['sellers'] = Seller.objects.filter(products__category__id=self.request.GET.get('category',None))
        else:
            context['categories'] = Category.objects.filter(parent__name='Строительный')
            context['sellers'] = Seller.objects.all()
            context['products'] = Product.objects.all()

        
        context['new_products'] = Product.objects.filter(type='NEW')
        # cat_id = self.request.GET.get('category',None)
        # print(cat_id)
        # print(self.requets.path)
        # if cat_id:
        #     products = Product.objects.filter(category=cat_id)
        #     context['products']  = products   
        #     print(products)
        # else:
        #     products = Product.objects.filter(category__parent__name='Строительный')
        #     context['products']  = products
        return context
    

class ProductTextView(ListView):
    queryset = queryset = Product.objects.all()
    template_name = 'catalog_text.html'
    context_object_name = 'products'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(parent__name='Строительный')
        if self.request.GET.get('seller', None) and self.request.GET.get('category',None):
            context['products'] = Product.objects.filter(seller=self.request.GET.get('seller'),category=self.request.GET.get('category',None))
            print(f"Products ------->  {Product.objects.filter(seller=self.request.GET.get('seller'),category=self.request.GET.get('category',None))}")
            context['categories'] = Category.objects.filter(products__seller=self.request.GET.get('seller', None))
            context['sellers'] = Seller.objects.all()
        elif self.request.GET.get('seller', None):
            print(self.request.GET.get('seller', None))
            context['sellers'] = Seller.objects.all()
            context['products'] = Product.objects.filter(seller=self.request.GET.get('seller', None))
            print(F"products -------> {context['products']}")
            context['categories'] = Category.objects.filter(products__seller=self.request.GET.get('seller', None))
            context['seller_id']=  Seller.objects.filter(id=self.request.GET.get('seller', None)).first().id
       
        elif self.request.GET.get('category',None):
            context['products'] = Product.objects.filter(category=self.request.GET.get('category',None))
            print(context['products'])
            context['categories'] = Category.objects.filter(parent__name='Строительный')
            context['sellers'] = Seller.objects.filter(products__category__id=self.request.GET.get('category',None))
        else:
            context['categories'] = Category.objects.filter(parent__name='Строительный')
            context['sellers'] = Seller.objects.all()
            context['products'] = Product.objects.all()

        
        context['new_products'] = Product.objects.filter(type='NEW')
        # cat_id = self.request.GET.get('category',None)
        # print(cat_id)
        # print(self.requets.path)
        # if cat_id:
        #     products = Product.objects.filter(category=cat_id)
        #     context['products']  = products   
        #     print(products)
        # else:
        #     products = Product.objects.filter(category__parent__name='Строительный')
        #     context['products']  = products
        return context
    

class HowToByView(ListView):
    queryset = Logistic.objects.all()
    template_name = 'logistics.html'
    context_object_name = 'logistics'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logistics_price'] = self.queryset.filter(id=self.request.GET.get('logistics',None)).last()
        print(self.request.GET.get('logistics',None))
        context['current_name'] = self.request.GET.get('logistics',None)
        print(context['current_name'])
        return context


class ContactView(TemplateView):
    template_name ='contact.html'


def export_excelView(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filenmae=Expenses' + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Expenses')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Name', 'Тип_измерения', 'Масса_за_1_шт','Цена']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    
    font_style = xlwt.XFStyle()
    
    cat_id = request.GET.get('category',None)
    rows = Product.objects.filter(category=5).values_list(
        'name', 'measurement_type','mass', 'price'
    )
    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)

    return response
