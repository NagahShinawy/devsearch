from django.db import models


class Make(models.Model):
    name = models.CharField(max_length=50)
    factory_address = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=20)
    active = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    make = models.ForeignKey(Make, on_delete=models.PROTECT, related_name="cars")

    def __str__(self):
        return self.name
