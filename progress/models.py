from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManager
from psycopg2 import DatabaseError

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


class Category(DateTimeMixin, MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, related_name='categories', null=True, blank=True)
    name = models.CharField(_('Имя'), max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    objects = TreeManager()

    
class Product(DateTimeMixin):
    class Product_Type(models.TextChoices):
        NEW = 'NEW', _('New')
        POPULAR = 'POP', _('Popular')
    
    class Price_Type(models.TextChoices):
        DOLLAR = 'DOL', _('Dollar',)
        EUR = 'EUR', _('Eur',)
        RUBLE = 'RUB', _('Ruble',)

    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    name = models.CharField(_('Имя'), max_length=100)
    seller = models.ForeignKey('Seller', on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(_('Изображение'), upload_to = 'product-images')
    price_type = models.CharField(_('Тип цены'), max_length=64, choices=Price_Type.choices)
    code = models.CharField(_('ИД(Code)'), max_length=64)
    measurement_type = models.CharField(_('Тип измерения'), max_length=64)
    mass = models.CharField(_('Масса за 1 шт'), max_length=64)
    all_mass = models.CharField(_('Вес 1 коробки'),max_length=64) 
    price  = models.FloatField(_('Цена'))
    description = models.TextField(_('Описание'))
    type = models.CharField(_('Тип'), choices=Product_Type.choices, max_length=64, null=True, blank=True)

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

