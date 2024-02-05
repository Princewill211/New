from django import forms
from .models import Article
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'type_of_articles', 'name_of_corresponding_author','email_of_corresponding_author','other_author_names','abstract','key_words','main_text', 'image',)

        widgets = {            
            'title':forms.TextInput(attrs={'class':'form-title-styling', 'placeholder':' Input Your Title'}),
            'type_of_articles':forms.Select(attrs={'class':'form-title-styling', 'placeholder':' Input Your Title'}),
            'name_of_corresponding_author':forms.TextInput(attrs={'class': 'form-name_of_corresponding_author-styling', 'placeholder':'write the corresponding author names'}),
            'email_of_corresponding_author':forms.TextInput(attrs={'class': 'form-email_of_corresponding_author-styling', 'placeholder':'corresponding authors email'}),
            'other_author_names':forms.TextInput(attrs={'class': 'form-other_author_names-styling', 'placeholder':' input other authors names'}),
            'abstract':forms.Textarea(attrs={'class': 'form-abstract-styling', 'placeholder':'input your Description' }),
            'key_words':forms.TextInput(attrs={'class': 'form-key_words-styling', 'placeholder':'write 5-6 keywords'}),
            'main_text':forms.Textarea(attrs={'class': 'form-main_text-styling', 'placeholder':'write your Introduction, Materials and methods, Results, Disscussion,Conclusion e.t.c'}),
            'image':forms.FileInput(attrs={'class': 'form-image-styling',}),
           
            
        }




# class   RegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']      


        













        






























        









































