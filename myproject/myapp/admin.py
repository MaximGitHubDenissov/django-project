from django.contrib import admin
from django.utils.safestring import mark_safe

from myapp.models import Product, Order, Client, Enrollment

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'add_date', 'get_image']
    ordering = ['-add_date']
    search_fields = ['name']
    search_help_text = 'Название продукта'


    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100", height="100"')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'date_ordered', 'total_order', 'enroll_in_order']


admin.site.register(Client)

