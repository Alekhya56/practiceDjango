from django import forms
 
from .models import Product_Model

class ProductForm(forms.ModelForm):
    title       = forms.CharField(label  = 'Title', widget = forms.TextInput(
                                  attrs  = {"placeholder": "Your Title" 
                                           }))
    description = forms.CharField(required = False, widget = forms.Textarea(
                                  attrs = { 'placeholder': "Your Description",
                                            'rows' : 8, 'cols' : 23
                                           }))
    price       = forms.DecimalField(initial=12.00)
    class Meta:
        model= Product_Model
        fields = ['title', 'description', 'price']
    # def clean_<my_field name>
    # def clean_title(self, *args, **kwargs): 
    #     title = self.cleaned_data.get("title")
    #     if "CFE" not in title:
    #         raise forms.ValidationError("This is not a valid Title")

class RawProductForm (forms.Form):
    title       = forms.CharField(
                        label  = 'Title', 
                        widget = forms.TextInput(
                                 attrs  = { 
                                     "placeholder": "Your Title"      
                                }
                            )
                        )
    description = forms.CharField(
                        required = False ,
                        widget   = forms.Textarea(
                                        attrs = {
                                            'placeholder': "Your Description",
                                            'rows' : 8,
                                            'cols' : 23
                                        }
                                    )           
                                )
    price       = forms.DecimalField(initial=12.00)