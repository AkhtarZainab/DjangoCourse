from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pid','pname','pcost','pmfdt','pexpdt']
    list_filter = ['pname','pmfdt','pexpdt']

    class meta:
        model = Product

admin.site.register(Product,ProductAdmin)