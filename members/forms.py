from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile





class UserForm(forms.ModelForm):
    class Meta:
        fields = [
            'username',
            'enail',
        ]






class userProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'is_author',
            'profile_image',
            ]