from django.shortcuts import render, redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from .forms import RegistartionForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import  login_required

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = RegistartionForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created and you can Log-in')
            return redirect('login')
    else:
        form = RegistartionForm()
    return render (request,'Users/register.html',{'form': form})

@login_required
def profile(request):
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
            'u_form': u_form,
            'p_form': p_form
            }

    return render(request, 'users/profile.html', context)


@login_required
def update_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, 'Users/profile_update.html',context)
