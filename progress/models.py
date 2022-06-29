
from gettext import translation
from venv import create
from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

class DateTimeMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class HomeImage(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_('Текст'), max_length=200),
        image = models.ImageField(_('Изображение'), upload_to = 'home-images')
    )
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Главная Изображение')
        verbose_name_plural = _('Главная Изображения')


class Category(DateTimeMixin):
    ParentType = (
        ('Строительный', 'Строительный'),
        ('Продукты', 'Продукты'),
        ('Текстильные' ,'Текстильные')
    )
    parent = models.CharField(_('Родитель'), max_length=100, choices=ParentType, null=True, blank=True)
    name = models.CharField(_('Имя'), max_length=100)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

   

class Product(TranslatableModel):
    class Product_Type(models.TextChoices):
        NEW = 'NEW', _('New')
        POPULAR = 'POP', _('Popular')
    
    class Price_Type(models.TextChoices):
        DOLLAR = 'DOL', _('Dollar',)
        EUR = 'EUR', _('Eur',)
        RUBLE = 'RUB', _('Ruble',)
    
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    seller = models.ForeignKey('Seller', on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(_('Изображение'), upload_to = 'product-images',null=True, blank=True)
    price_type = models.CharField(_('Тип цены'), max_length=64, choices=Price_Type.choices,null=True, blank=True)
    code = models.CharField(_('ИД(Code)'), max_length=64,null=True, blank=True)
    measurement_type = models.CharField(_('Тип измерения'), max_length=64,null=True, blank=True)
    mass = models.CharField(_('Масса за 1 шт'), max_length=64,null=True, blank=True)
    all_mass = models.CharField(_('Вес 1 коробки'),max_length=64,null=True, blank=True) 
    price  = models.FloatField(_('Цена'),null=True, blank=True)
    slug = models.SlugField(_('Slug'), max_length=100,null=True, blank=True)
    type = models.CharField(_('Тип'), choices=Product_Type.choices, max_length=64, null=True, blank=True)
    name = models.CharField(_('Имя'), max_length=100)
    translations = TranslatedFields(
        description = models.TextField(_('Описание'),null=True, blank=True),
        title = models.CharField(_('Название1'),max_length = 200, null=True,blank=True),
        value = models.CharField(_('Ценность1'),max_length = 100,null=True,blank=True),
        title1 = models.CharField(_('Название1'), max_length=100,null=True,blank=True),
        value1 = models.CharField(_('Ценность1'), max_length=200,null=True,blank=True),
        title2 = models.CharField(_('Название2'), max_length = 200,null=True,blank=True),
        value2 = models.CharField(_('Ценность2'), max_length = 100,null=True,blank=True),
        title3 = models.CharField(_('Название3'), max_length=100,null=True,blank=True),
        value3 = models.CharField(_('Ценность3'), max_length=200,null=True,blank=True),
        title4 = models.CharField(_('Название4'), max_length = 200,null=True,blank=True),
        value4 = models.CharField(_('Ценность4'), max_length = 100,null=True,blank=True),
        title5 = models.CharField(_('Название5'), max_length=100,null=True,blank=True),
        value5 = models.CharField(_('Ценность5'), max_length=200,null=True,blank=True),
        title6 = models.CharField(_('Название6'), max_length = 200, null=True,blank=True),
        value6 = models.CharField(_('Ценность6'), max_length = 100,null=True,blank=True),
        title7 = models.CharField(_('Название7'), max_length=100,null=True,blank=True),
        value7 = models.CharField(_('Ценность7'), max_length=200,null=True,blank=True),
        title8 = models.CharField(_('Название8'), max_length = 200,null=True,blank=True),
        value8 = models.CharField(_('Ценность8'), max_length = 100,null=True,blank=True),
        title9 = models.CharField(_('Название9'), max_length=100,null=True,blank=True),
        value9 = models.CharField(_('Ценность9'), max_length=200,null=True,blank=True),
        title10 = models.CharField(_('Название10'),max_length = 200,null=True,blank=True),
        value10 = models.CharField(_('Ценность10'), max_length = 100,null=True,blank=True),
    )
    def __str__(self):  
        return str(self.code)
    
    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')
        
class NewProduct(TranslatableModel):
    class Product_Type(models.TextChoices):
        NEW = 'NEW', _('New')
        POPULAR = 'POP', _('Popular')
    class Price_Type(models.TextChoices):
        DOLLAR = 'DOL', _('Dollar',)
        EUR = 'EUR', _('Eur',)
        RUBLE = 'RUB', _('Ruble',)
    translations = TranslatedFields(

        name = models.CharField(_('Имя'), max_length=100),
    )
    price  = models.FloatField(_('Цена'),null=True, blank=True)
    type = models.CharField(_('Тип'), choices=Product_Type.choices, max_length=64, null=True, blank=True)
    image = models.ImageField(_('Изображение'), upload_to = 'product-images',null=True, blank=True)
    price_type = models.CharField(_('Тип цены'), max_length=64, choices=Price_Type.choices,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):  
        return self.name
    
    class Meta:
        verbose_name = _('Новый Товар')
        verbose_name_plural = _('Новый Товары')

class Certificate(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_('Имя'), max_length=100),
        image = models.ImageField(_('Изображение'), upload_to = 'certificate-images')
    )
    def __str__(self):
        return str(self.name)
    
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

class Customer(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_('Имя'), max_length=64),
        description = models.TextField(_('Text'))
    )
    image = models.ImageField(_('Изображение'), upload_to = 'customers-images')
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Покупатель')
        verbose_name_plural = _('Клиенты')

class Seller(DateTimeMixin):
    name = models.CharField(_('Имя'), max_length=64)
    image = models.ImageField(_('Изображение'), upload_to = 'seller-images', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
   

class Logistic(TranslatableModel):
    translations = TranslatedFields(
        place_name = models.CharField(_('Куда'), max_length=100),
        price = models.CharField(_('Цена'), max_length=64)
    )
    def __str__(self):
        return self.place_name
    
    class Meta:
        verbose_name = _('Логистика')
        verbose_name_plural = _('Логистика')


class FileModel(DateTimeMixin):
    upload = models.FileField(upload_to='products_informations_files')

    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = _('Файл продукта')
        verbose_name_plural = _('Файлы продукта')


class PriceExcelModel(DateTimeMixin):
    upload = models.FileField(upload_to="price_excel")

    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = _('Kонтрагентов документ')
        verbose_name_plural = _('Kонтрагентов документы')


class Brend(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_('Имя'), max_length=100),
        description = models.TextField(_('Text'))
    )
    image = models.ImageField(_('Изображение'), upload_to = 'brend-images')
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Спонсор')
        verbose_name_plural = _('Спонсоры')

class CatalogImage(DateTimeMixin):
    name = models.CharField(_('Имя'), max_length=100)
    image = models.ImageField(_('Изображение'), upload_to = 'certificate-images')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Каталог Страница Изображение')
        verbose_name_plural = _('Каталог Страница Изображения')