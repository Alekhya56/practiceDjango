from typing import Any, Union

from django import forms
from .models import ItemList

def get_default_count():
    try:
        p = ItemList.objects.latest('sno')
        return int(p.sno) + 1
    except:
        p= 0
        return int(p) + 1

class AddItemForm(forms.ModelForm):

    sno = forms.IntegerField(initial= get_default_count, required=True)
    # widget = forms.TextInput(attrs={'required': 'true'}),

    item_name = forms.CharField(label='Item', required=True)

    amount = forms.IntegerField(required=True)

    class Meta:
        model = ItemList
        fields = ['sno', 'item_name', 'amount']



        # < label
        # for ="sno" > sno < input type = "text" name="sno" > < / label >
        # < br >
        # < label
        # for ="sno" > Item Name < input type = "text" name="Item" > < / label >
        # < br > < label
        # for ="sno" > Price < input type = "text" name="price" > < / label >