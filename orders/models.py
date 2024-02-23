from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        """Return a string representation of the model."""
        return self.name

class Order(models.Model):
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def update_total_price(self):
        self.total_price = sum(product.price for product in self.products.all())
        self.save()

    def __str__(self):
        return f"Order {self.id}: Total Price - {self.total_price}"
    

# order = Order.objects.create()
# product1 = Product.objects.create(name='Product 1', price=10.99)
# product2 = Product.objects.create(name='Product 2', price=5.99)

# order.products.add(product1, product2)
# order.update_total_price()