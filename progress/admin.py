
from django.contrib.auth.models import Group, User
from django.contrib import admin
from progress.models import FileModel, HomeImage, Category,Brend ,Certificate,PriceExcelModel, Product, Gallery, Seller, Customer, Logistic
from import_export.admin import ImportExportModelAdmin



admin.site.register(Brend)



@admin.register(HomeImage)
class HomeImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category)

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    pass

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Logistic)
class LogisticAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(ImportExportModelAdmin):
    list_display = ('name', 'code', 'mass', 'all_mass','price')
admin.site.register(Product)

admin.site.register(Certificate)


admin.site.register(Gallery)

admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(FileModel)
admin.site.register(PriceExcelModel)
