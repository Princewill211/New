from django.shortcuts import render, redirect
from django.views import generic 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout
from django.urls import reverse_lazy
from . import views
from .forms import UserForm, userProfileForm
# imports for userprofile
# from django.http import HttpResponseRedirect
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib import messages
# from django.contrib.auth.models import User
# from members.models import UserProfile
# from django.views.generic import TemplateView


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
        



# class UserProfile(LoginRequiredMixin, TemplateView):
#     template_name = 'registration/profile.html'


# class UserProfileUpdate(LoginRequiredMixin, TemplateView):
#     user_form = UserForm 
#     profile_form = userProfileForm
#     template_name = 'registration/profile-update.html'

#     def post(self, request):

#         post_data = request.POST or None
#         file_data = request.FILES or None


#         user_form=UserForm(post_data, instance=request.user)
#         profile_form=UserForm(post_data, file_data, instance=request.user.UserProfile)

#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Your profile was successfully updated')
#             return HttpResponseRedirect(reverse_lazy('UserProfile'))
        
#         context = self.get_context_data(
#                                        user_form=user_form,
#                                        profile_form=profile_form
#                                        )
        
#         return self.render_to_response(context)
    
#     def get(self, request, *args, **kwargs):
#         return self.post(request, *args, **kwargs)













def UserProfile(request, pk):
    return render(request, 'registration/profile.html')
 

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
