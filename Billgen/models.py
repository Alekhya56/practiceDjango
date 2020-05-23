from django.db import models

# Create your models here.
def get_default_count():
    p = ItemList.objects.latest('sno')
    return int(p.sno) + 1

class ItemList(models.Model):

    sno = models.IntegerField(unique= True, default= get_default_count, blank= False)
    item_name = models.CharField(max_length = 20, blank= False,)
    amount = models.IntegerField(blank = False)

    def __str__(self):
        return f"{self.sno},{self.item_name},{self.amount}"

    class Meta:
        ordering = ['sno']
