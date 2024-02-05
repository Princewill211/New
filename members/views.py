from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout
from django.urls import reverse_lazy
from . import views
from .forms import userProfileForm


# Create your views here.


# class UserRegisterView(generic.CreateView):
#     form_class = UserCreationForm
#     template_name = 'registration/register.html'
#     success_url = reverse_lazy('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        profile_form =  userProfileForm(request.POST)
        
        if form.is_valid() and profile_form.is_valid():
            user=form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()




            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            access = authenticate(username=username, password=password)
            login(request, user)

            return redirect('login')
    else:
        form = UserCreationForm()
        profile_form =  userProfileForm()
        
    context ={'form':form, 'profile_form':profile_form}
    return render(request, 'registration/register.html', context)
        


def UserProfile(request, pk):
    return render(request, 'registration/user_profile.html')
 

# def Register(request):
#     form = RegisterForm(request.POST)
#     if form.is_valid:
#         pass
#     else:
#         form = RegisterForm()

#     context = {
#         'form':form
#     }
#     return render(request,'registration/register.html', context ) 

def logout_user(request):
    logout(request)
    return redirect('home')
