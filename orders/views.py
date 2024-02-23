from django.shortcuts import render
from .models import Product, Order
from django.contrib.auth.decorators import login_required

def menu_view(request):
    products = Product.objects.all()
    context = {'products' : products}
    return render(request, 'orders/menu_view.html', context)
@login_required
def order_view(request):
    if request.method == 'POST':
        product_ids = request.POST.getlist('product')
        products = list(Product.objects.filter(pk__in=product_ids))
        
        order = Order.objects.create(owner=request.user)
        order.products.set(products)
        order.update_total_price()

        return render(request, 'orders/order_confirmation.html', {'order': order})

    products = Product.objects.all()
    return render(request, 'orders/order.html', {'products': products})