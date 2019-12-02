from django.db import models
from django.urls import reverse
# Create your models here.
class Product_Model(models.Model):
    title       = models.CharField(max_length = 120)
    description = models.TextField(default = "This is a Fruit")
    price       = models.DecimalField(max_digits = 5, decimal_places =2)
    summary     = models.TextField(blank = True, null = True)
    def get_absolute_url(self):
        return reverse("Products:dynamic",kwargs= {"my_id" : self.id})