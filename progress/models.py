
from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel


class DateTimeMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class HomeImage(DateTimeMixin):
    title = models.CharField(_('Текст'), max_length=200)
    image = models.ImageField(_('Изображение'), upload_to = 'home-images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Главная Изображение')
        verbose_name_plural = _('Главная Изображения')


class Category(DateTimeMixin):
    type = (
        ('Строительный','Строительный'),
        ('Продукты', 'Продукты'),
        ('Текстильные','Текстильные'),
    )
    parent = models.CharField(max_length=100, choices=type)
    name = models.CharField(_('Имя'), max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

   

    
class Product(DateTimeMixin):
    class Product_Type(models.TextChoices):
        NEW = 'NEW', _('New')
        POPULAR = 'POP', _('Popular')
    
    class Price_Type(models.TextChoices):
        DOLLAR = 'DOL', _('Dollar',)
        EUR = 'EUR', _('Eur',)
        RUBLE = 'RUB', _('Ruble',)

    category = models.ForeignKey('Category', on_delete=models.SET_NULL, related_name='products',null=True, blank=True)
    name = models.CharField(_('Имя'), max_length=100, null=True, blank=True)
    seller = models.ForeignKey('Seller', on_delete=models.SET_NULL, related_name='products',null=True, blank=True)
    image = models.ImageField(_('Изображение'), upload_to = 'product-images',null=True, blank=True)
    price_type = models.CharField(_('Тип цены'), max_length=64, choices=Price_Type.choices,null=True, blank=True)
    code = models.CharField(_('ИД(Code)'), max_length=64,null=True, blank=True)
    measurement_type = models.CharField(_('Тип измерения'), max_length=64,null=True, blank=True)
    mass = models.CharField(_('Масса за 1 шт'), max_length=64,null=True, blank=True)
    all_mass = models.CharField(_('Вес 1 коробки'),max_length=64,null=True, blank=True) 
    price  = models.FloatField(_('Цена'),null=True, blank=True)
    slug = models.SlugField(_('Slug'), max_length=100,null=True, blank=True)
    description = models.TextField(_('Описание'),null=True, blank=True)
    type = models.CharField(_('Тип'), choices=Product_Type.choices, max_length=64, null=True, blank=True)
    title = models.CharField(max_length = 200, null=True,blank=True)
    value = models.CharField(max_length = 100,null=True,blank=True)
    title1 = models.CharField(max_length=100,null=True,blank=True)
    value1 = models.CharField(max_length=200,null=True,blank=True)
    title2 = models.CharField(max_length = 200,null=True,blank=True)
    value2 = models.CharField(max_length = 100,null=True,blank=True)
    title3 = models.CharField(max_length=100,null=True,blank=True)
    value3 = models.CharField(max_length=200,null=True,blank=True)
    title4 = models.CharField(max_length = 200,null=True,blank=True)
    value4 = models.CharField(max_length = 100,null=True,blank=True)
    title5 = models.CharField(max_length=100,null=True,blank=True)
    value5 = models.CharField(max_length=200,null=True,blank=True)
    title6 = models.CharField(max_length = 200, null=True,blank=True)
    value6 = models.CharField(max_length = 100,null=True,blank=True)
    title7 = models.CharField(max_length=100,null=True,blank=True)
    value7 = models.CharField(max_length=200,null=True,blank=True)
    title8 = models.CharField(max_length = 200,null=True,blank=True)
    value8 = models.CharField(max_length = 100,null=True,blank=True)
    title9 = models.CharField(max_length=100,null=True,blank=True)
    value9 = models.CharField(max_length=200,null=True,blank=True)
    title10 = models.CharField(max_length = 200,null=True,blank=True)
    value10 = models.CharField(max_length = 100,null=True,blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')
        

class Certificate(DateTimeMixin):
    name = models.CharField(_('Имя'), max_length=100)
    image = models.ImageField(_('Изображение'), upload_to = 'certificate-images')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Сертификат')
        verbose_name_plural = _('Сертификаты')


class Gallery(DateTimeMixin):
    name = models.CharField(_('Имя'), max_length=100)
    image = models.ImageField(_('Изображение'), upload_to = 'certificate-images')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Галерея')
        verbose_name_plural = _('Галереи')

class Customer(DateTimeMixin):
    name = models.CharField(_('Имя'), max_length=64)
    image = models.ImageField(_('Изображение'), upload_to = 'customers-images')
    description = models.TextField(_('Text'))
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Покупатель')
        verbose_name_plural = _('Клиенты')

class Seller(DateTimeMixin):
    name = models.CharField(_('Имя'), max_length=64)
    image = models.ImageField(_('Изображение'), upload_to = 'seller-images')
    description = models.TextField(_('Text'))
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Производитель')
        verbose_name_plural = _('Производители')

class Logistic(DateTimeMixin):
    place_name = models.CharField(_('Куда'), max_length=100)
    price = models.CharField(_('Цена'), max_length=64)

    def __str__(self):
        return self.place_name
    
    class Meta:
        verbose_name = _('Логистика')
        verbose_name_plural = _('Логистика')


class FileModel(DateTimeMixin):
    upload = models.FileField(upload_to='products_informations_files')

    def __str__(self):
        return str(self.id)



class PriceExcelModel(DateTimeMixin):
    upload = models.FileField(upload_to="price_excel")

    def __str__(self):
        return str(self.id)

class Brend(DateTimeMixin):
    name = models.CharField(_('Имя'), max_length=100)
    image = models.ImageField(_('Изображение'), upload_to = 'brend-images')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Brend')
        verbose_name_plural = _('Bredns')

class CatalogImage(DateTimeMixin):
    name = models.CharField(_('Имя'), max_length=100)
    image = models.ImageField(_('Изображение'), upload_to = 'certificate-images')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('CatalogImage')
        verbose_name_plural = _('CatalogImages')