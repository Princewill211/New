from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.



class Article(models.Model):
     title = models.CharField(max_length=200)
     article_choices = {
          ('Research article','Research article'),
          ('Review article','Review article'),
          ('Short communication','Short communication'),
     }
     type_of_articles = models.CharField(max_length=200, blank=True, null=True, choices=article_choices)
     name_of_corresponding_author = models.CharField(max_length=200, default='')
     email_of_corresponding_author = models.EmailField(max_length=200)
     other_author_names = models.CharField(max_length=250, default='')
     abstract = models.CharField(max_length=220, default='' )
     key_words = models.CharField(max_length=200)
     main_text = RichTextField(blank=True, null=True)
     # main_text = models.TextField(null=True, blank=True)
     image = models.ImageField(upload_to='uploads/article_images',blank='True', null='True')
     pdf_upload = models.FileField(upload_to='uploads/article_images/pdf',blank='True', null='True')
     published= models.BooleanField(default=False)
     updated = models.DateTimeField(auto_now=True)
     created = models.DateTimeField(auto_now_add=True)


     class Meta:
          ordering = [ '-updated', '-created']


     def __str__(self):
          return self.name_of_corresponding_author + ' | '  + str(self.title) 
     

     def get_absolute_url(self):
          return reverse('home')
          # return reverse('article-detail', args=(str(self.id)))
          