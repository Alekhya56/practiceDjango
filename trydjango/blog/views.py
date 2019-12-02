from django.shortcuts import render, get_object_or_404

from django.urls import reverse

# Create your views here.
from .forms import ArticalModelForm

from django.views.generic import (
                    ListView,
                    CreateView,
                    UpdateView,
                    DeleteView,
                    DetailView
)

from .models import ArticalModel

class ArticalCreateView(CreateView):
    template_name = 'blog/articalmodel_create.html'
    form_class = ArticalModelForm
    queryset = ArticalModel.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticalListView(ListView):
    template_name = 'blog/articalmodel_list.html' # it looks for appname/modelname_viewname.html
    queryset = ArticalModel.objects.all()

class  ArticalDetailView(DetailView):
    template_name = 'blog/articalmodel_detail.html'
    
    def get_object(self):
        id_ = self.kwargs.get("id") 
        return get_object_or_404(ArticalModel, id = id_)

class ArticalDeleteView(DeleteView):
    template_name = 'blog/articalmodel_delete.html'
    
    def get_object(self):
        my_id = self.kwargs.get('id') 
        return get_object_or_404(ArticalModel, id = my_id)
    
    def get_success_url(self):
        return reverse('blog:list')

class ArticalUpdateView(UpdateView):
    template_name = 'blog/articalmodel_create.html'
    form_class = ArticalModelForm
    queryset = ArticalModel.objects.all()

    def get_object(self):
        my_id = self.kwargs.get('id') 
        return get_object_or_404(ArticalModel, id = my_id)
    
    def form_valid(self, form):
        return super().form_valid(form) 