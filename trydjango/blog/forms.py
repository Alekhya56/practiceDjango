from django import forms

from .models import ArticalModel

class ArticalModelForm(forms.ModelForm):
    artical_name     = forms.CharField(label = "Artical Name", widget = forms.TextInput(
                                       attrs= { "place_holder": "Enter the Artical name"}
                                       ))
    author_name      = forms.CharField(label = "Author Name", widget = forms.TextInput(
                                       attrs= { "place_holder":"Enter the Author's name"}
                                       ))
    description = forms.CharField(required= False, widget = forms.Textarea(
                                       attrs = {'rows': 10,
                                                'cols' : 25}
                                       ))
    price       = forms.DecimalField(initial = 200.00)

    class Meta:
        model = ArticalModel
        fields = ['artical_name', 'author_name','description','price']


# class ArticalForm(forms.Form):
#     artical_name     = forms.CharField(label = "Artical Name", widget = forms.TextInput(
#                                        attrs= { "place_holder": "Enter the Artical name"}
#                                        ))
#     author_name      = forms.CharField(label = "Author Name", widget = forms.TextInput(
#                                        attrs= { "place_holder":"Enter the Author's name"}
#                                        ))
#     description      = forms.charField(required= False, widget = forms.Textarea(
#                                        attrs = {'rows': 10,
#                                                 'cols' : 25}
#                                        ))
#     price            = forms.DecimalField(inital = 200.00)