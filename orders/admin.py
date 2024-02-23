from django.contrib import admin
from .models import Product, Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_price',)

    def save_model(self, request, obj, form, change):
        # Save the order without the many-to-many relationship
        super().save_model(request, obj, form, change)
        # Add products to the order
        products = form.cleaned_data.get('products')# Assuming you have a products field in your form
        obj.products.set(products)

        # Update the total price
        obj.update_total_price()

admin.site.register(Order, OrderAdmin)
admin.site.register(Product) 


