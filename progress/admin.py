
from django.contrib.auth.models import Group, User
from django.contrib import admin
from progress.models import HomeImage, Category, Certificate, Product, Gallery, Seller, Customer, Logistic

@admin.register(HomeImage)
class HomeImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    pass

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Logistic)
class LogisticAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product)

admin.site.register(Certificate)


admin.site.register(Gallery)

admin.site.unregister(Group)
admin.site.unregister(User)
