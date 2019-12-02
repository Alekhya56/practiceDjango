from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from django.http import Http404

from .models import Product_Model

from .forms import ProductForm, RawProductForm
 
def dynamic_lookup_view(request, my_id):
    #obj = Product_Model.objects.get(id = my_id)
    #obj = get_object_or_404(Product_Model, id =my_id)
    try:
        obj = Product_Model.objects.get(id = my_id)
    except Product_Model.DoesNotExist:
        raise Http404
    my_context= {
        'obj': obj
    }
    return render(request, "Product\product_detail.html", my_context)

def render_initial_data(request):
    initial_data= {
        'title': "This is initial Title"
    }
    # To set initial data in the form
    # my_form = RawProductForm(request.POST or None ,initial=initial_data)
    # To change the objects details, frist get the obj and form should be imported from ModelForm
    obj = Product_Model.objects.get(id=1)
    my_form = ProductForm(request.POST or None,instance=obj)
    if my_form.is_valid():
        my_form.save()
        my_form = ProductForm()
    my_context = {
        'form': my_form
    }
    return render(request, "Product\product_create.html", my_context)

def product_create_view(request):
    my_form = RawProductForm(request.POST or None)
    if my_form.is_valid():
        # Here the cleaned data means the data after validation
        print(my_form.cleaned_data)
        # Product_Model.objects.create(Title= new_item_title)
        # create Objects in database
        # cleaned_data gives data in dictionary format
        Product_Model.objects.create(**my_form.cleaned_data)
    else:        
        print(my_form.errors)
    
    my_context = {
        'form': my_form
    }
    return render(request, "Product\product_create.html", my_context)

# def product_create_view(request):
#     print(request.GET)
#     print(request.POST)
#     new_title = request.POST.get('title')
#     print(new_title)
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     my_context = {
#         'form': form
#     }
#     return render(request, "Product\product_create.html", my_context)

# def product_create_view(request):
#     initial_data= {
#         'title': "This is initial Title"
#     }
#     form = ProductForm(request.POST or None ,initial_data)
#     if form.is_valid():
#         form.save()

#     my_context = {
#         'form': form
#     }
#     return render(request, "Product\product_create.html", my_context)

def product_delete_view(request,my_id):
    obj = get_object_or_404(Product_Model, id = my_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    my_context = {
        'obj': obj
    }
    return render(request, "Product\product_delete.html",my_context)

def product_list_view(request):
    queryset = Product_Model.objects.all()
    my_context ={
        'object': queryset
    }
    return render(request, "Product\product_list.html", my_context)

def product_detail_view(request,my_id): #(*args, **kwargs)
    objct = Product_Model.objects.get(id = my_id)
    # my_context={
    #     Title : obj.Title,
    #     Price : obj.Price,
    #     Description :obj.Description
    #     summary = obj.summary
    # }

    my_context = {
        'obj' : objct
    }
    return render (request,"Product\product_detail.html",my_context)
