from django.db import models

from django.urls import reverse
# Create your models here.
class ArticalModel(models.Model):
    artical_name      = models.CharField(max_length = 20)
    author_name       = models.CharField(max_length = 20)
    description  = models.CharField(max_length = 25)
    price        = models.DecimalField(max_digits = 5, decimal_places =2)
    def get_absolute_url(self):
        return reverse("blog:detail", kwargs = {'id':self.id})