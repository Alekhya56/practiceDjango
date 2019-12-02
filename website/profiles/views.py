from django.shortcuts import render, redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from .forms import RegistartionForm
from django.contrib.auth.decorators import  login_required

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = RegistartionForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            #username = request.POST['username']
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created and you can Log-in')
            return redirect('/../login/')
    else:
        form = RegistartionForm()
    return render (request,'register.html',{'form': form})

@login_required
def profile(request):
    return render(request, "profile.html")