from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0) 
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Option(models.Model):
    name = models.CharField(max_length=255)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    extra_price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
    

# Category: represents a menu category (e.g., appetizers, main courses).
# MenuItem: represents an individual item on the menu, associated with a category. It includes fields for the item's name, description, price, and an optional image.
# Option: represents additional options or customizations for a menu item.