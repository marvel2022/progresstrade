from distutils.command.upload import upload
from itertools import product
from unicodedata import category
from urllib import response

from django.http import HttpResponse
from progress.models import HomeImage,CatalogImage, Logistic,Brend, PriceExcelModel,Product, Category, Certificate, Gallery, Customer, Seller
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
import xlwt
from datetime import datetime

class HomeView(ListView):
    queryset = HomeImage.objects.all()
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(type='NEW')[:8]
        context['popular_products'] = Product.objects.filter(type='POP')[:8]
        return context
  


class AboutView(ListView):
    queryset = Gallery.objects.all()
    template_name = 'about.html'
    context_object_name = 'galeries'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['certificates'] = Certificate.objects.all()[:8]
        context['pricefile'] = PriceExcelModel.objects.all().last()
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
    queryset = Brend.objects.all()[:8]
    template_name = 'sellers.html'
    context_object_name = 'sellers'

class SellerDetailView(DetailView):
    queryset = Brend.objects.all()
    template_name = 'seller_detail.html'
    context_object_name = 'seller'




class CatalogConstructionView(ListView):
    queryset = Product.objects.all()
    template_name = 'catalog_construction.html'
    context_object_name = 'products1'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(parent='Строительный')
        context['bacground'] = CatalogImage.objects.filter(name='Строительный').last()
        if self.request.GET.get('seller', None) and self.request.GET.get('category',None):
            context['products'] = Product.objects.filter(seller=self.request.GET.get('seller'),category=self.request.GET.get('category',None))
            print(f"Products ------->  {Product.objects.filter(seller=self.request.GET.get('seller'),category=self.request.GET.get('category',None))}")
            context['categories'] = Category.objects.filter(products__seller=self.request.GET.get('seller', None))
            context['sellers'] = Seller.objects.all()
            context['cat_id'] = Category.objects.filter(id = self.request.GET.get('category',None)).first().id
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
            context['categories'] = Category.objects.filter(type='Строительный')
            context['sellers'] = Seller.objects.all()
            context['cat_id'] = Category.objects.filter(id = self.request.GET.get('category',None)).first().id
        else:
            context['categories'] = Category.objects.filter(parent='Строительный')
            context['sellers'] = Seller.objects.filter(products__category__parent='Строительный')
            context['products'] = Product.objects.filter(category__parent='category__parent')
        
        
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
        context['categories'] = Category.objects.filter(parent='Продукты')
        context['bacground'] = CatalogImage.objects.filter(name='Продукты').last()
        if self.request.GET.get('seller', None) and self.request.GET.get('category',None):
            context['products'] = Product.objects.filter(seller=self.request.GET.get('seller'),category=self.request.GET.get('category',None))
            print(f"Products ------->  {Product.objects.filter(seller=self.request.GET.get('seller'),category=self.request.GET.get('category',None))}")
            context['categories'] = Category.objects.filter(products__seller=self.request.GET.get('seller', None))
            context['sellers'] = Seller.objects.all()
            context['cat_id'] = Category.objects.filter(id = self.request.GET.get('category',None)).first().id
        elif self.request.GET.get('seller', None):
            print(self.request.GET.get('seller', None))
            context['sellers'] = Seller.objects.all()
            context['products'] = Product.objects.filter(seller=self.request.GET.get('seller', None), category__parent__name = 'Продукты')
            print(F"products -------> {context['products']}")
            context['categories'] = Category.objects.filter(products__seller=self.request.GET.get('seller', None), parent__name='Продукты')
            context['seller_id']=  Seller.objects.filter(id=self.request.GET.get('seller', None)).first().id
        
        elif self.request.GET.get('category',None):
            context['products'] = Product.objects.filter(category=self.request.GET.get('category',None))
            print(context['products'])
            context['categories'] = Category.objects.filter(parent='Продукты')
            context['sellers'] = Seller.objects.all()
            context['cat_id'] = Category.objects.filter(id = self.request.GET.get('category',None)).first().id
        else:
            context['categories'] = Category.objects.filter(parent='Продукты')
            context['sellers'] = Seller.objects.filter(products__category__parent='Продукты')
            context['products'] = Product.objects.filter(category__parent= 'Продукты')
        
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
        context['categories'] = Category.objects.filter(parent='Текстильные')

        context['bacground'] = CatalogImage.objects.filter(name='Текстильные').last()
        if self.request.GET.get('seller', None) and self.request.GET.get('category',None):
            context['products'] = Product.objects.filter(seller=self.request.GET.get('seller'),category=self.request.GET.get('category',None))
            print(f"Products ------->  {Product.objects.filter(seller=self.request.GET.get('seller'),category=self.request.GET.get('category',None))}")
            context['categories'] = Category.objects.filter()
            context['sellers'] = Seller.objects.all()
            context['cat_id'] = Category.objects.filter(id = self.request.GET.get('category',None)).first().id
        elif self.request.GET.get('seller', None):
            print(self.request.GET.get('seller', None))
            context['sellers'] = Seller.objects.all()
            context['products'] = Product.objects.filter(seller=self.request.GET.get('seller', None),category__parent__name = 'Текстильные' )
            print(F"products -------> {context['products']}")
            context['categories'] = Category.objects.filter(products__seller=self.request.GET.get('seller', None))
            context['seller_id']=  Seller.objects.filter(id=self.request.GET.get('seller', None)).first().id
            
        elif self.request.GET.get('category',None):
            context['products'] = Product.objects.filter(category=self.request.GET.get('category',None))
            print(context['products'])
            context['categories'] = Category.objects.filter(type='Текстильные')
            context['sellers'] = Seller.objects.all()
            context['seller_id'] = 0
            context['cat_id'] = Category.objects.filter(id = self.request.GET.get('category',None)).first().id
        else:
            context['categories'] = Category.objects.filter(parent='Текстильные')
            context['sellers'] = Seller.objects.filter(products__category__parent='Текстильные')
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
        context['logistics_price'] = self.queryset.filter(place_name=self.request.GET.get('logistic',None)).last()
        print(self.request.GET.get('logistic',None))
        context['current_name'] = self.request.GET.get('logistic',None)
        print(f"this is name------> {context['current_name']}")
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
    print(f"id--------> {cat_id}")
    if cat_id:
        rows = Product.objects.filter(category=cat_id).values_list(
            'name', 'measurement_type','mass', 'price'
        )
    else:
        rows = Product.objects.all().values_list(
        'name', 'measurement_type','mass', 'price'
        )
    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)

    return response













from .resources import ProductResource
from django.contrib import messages

from tablib import Dataset
from django.http import HttpResponse

def simple_upload(request):
    if request.method == "POST":
        product_resource = ProductResource()
        dataset = Dataset()
        print(f"request - files ------> {request.FILES['myfile']}")
        new_product = request.FILES['myfile']
        print(f" file ---------> {new_product}")
        if not new_product.name.endswith('xlsx'):
            messages.info(request, "wrong format")
            return render(request, 'upload.html')
        imported_data = dataset.load(new_product.read(), format='xlsx')
        for data in imported_data:
            value = Product(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
               
            )
            value.save()
            print(value)

    return render(request, 'upload.html')


