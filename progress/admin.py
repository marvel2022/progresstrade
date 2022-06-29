from django.contrib.auth.models import Group, User
from django.contrib import admin
from progress.models import FileModel,CatalogImage, NewProduct, HomeImage, Category,Brend ,Certificate,PriceExcelModel, Product, Gallery, Seller, Customer, Logistic
from import_export.admin import ImportExportModelAdmin
from parler.admin import TranslatableAdmin


@admin.register(Brend)
class BrendAdmin(TranslatableAdmin):
    pass


@admin.register(HomeImage)
class HomeImageAdmin(TranslatableAdmin):
    pass

admin.site.register(Category)


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    pass

@admin.register(Customer)
class CustomerAdmin(TranslatableAdmin):
    pass


@admin.register(Logistic)
class LogisticAdmin(TranslatableAdmin):
    pass

@admin.register(NewProduct)
class NewProductAdmin(TranslatableAdmin):
    pass


@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ('name', 'code', 'mass', 'all_mass','price')

admin.site.register(Certificate)

admin.site.register(CatalogImage)

admin.site.register(Gallery)

admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(FileModel)
admin.site.register(PriceExcelModel)
