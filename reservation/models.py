from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    num_guests = models.PositiveIntegerField()
    special_requests = models.TextField(blank=True, null=True) 

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"
