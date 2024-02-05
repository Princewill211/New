from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect,HttpResponse
from .pdf import html2pdf
# from django.http import HttpResponse
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from django.db.models import Q
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.forms import UserCreationForm 
from .models import Article 
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import ArticleForm
from django.urls import reverse_lazy

# Create your views here.



# def loginPage(request):
#     page = 'login'
#     if request.user.is_authenticated:
#        return redirect('home')
   
#     if request.method == 'POST':
#         username = request.POST.get('username').lower()       
#         password = request.POST.get('password')
#         print(username, password)

#         try:
#             user = User.objects.get(username=username)
#         except:
#             messages.error(request, 'user does not exsit')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#            login(request, user)
#            return redirect('home')
#         else:
#            messages.error(request, 'Username OR password does not exsit')

#     context = {'page':page}
#     return render(request, 'base/login_register.html', context)


# def logoutUser(request):
#     logout(request)
#     return redirect('home')


# def registerPage(request):
#     form = UserCreationForm()

#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#            user = form.save(commit=False)
#            user.username = user.username.lower()
#            user.save()
#            login(request, user)
#            return redirect('home')
#         else:
#            messages.error(request, 'An error occured during registration')
        
#     return render(request, 'base/login_register.html', {'form':form})




# def HomePageView(request):
#     queryset = Article.objects.all()
#     q = request.GET.get('q') if request.GET.get('q') != None else ''
#     articles1 = Article.objects.filter(
#     Q(name_of_corresponding_author__icontains=q) |
#     Q(main_text__icontains=q) |
#     Q(title__icontains=q)
#     )
#     context = {'object_list':queryset,'articles1':articles1}
#     return render(request, 'base/home.html', context) 


class HomeView(ListView):
    model = Article
    template_name = 'base/home.html'
    ordering = [ '-updated', '-created']
    context_object_name='image'

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().exclude(published=False)


class ArticleDetailView( DetailView):  
    model = Article 
    # pdf=html2pdf('base/article_detail.html')
    # content_type="application/pdf"
    template_name = 'base/article_detail.html'

    def pdf(request):
        pdf=html2pdf(template_name)
        template_name = 'base/article_detail.html'
        return HttpResponse(pdf,content_type="application/pdf") 
    


class AddArticleView(CreateView):
    model = Article 
    form_class = ArticleForm
    template_name = 'base/add_article.html'
    # fields = ('title_of_article ',  'name ','email','description ','excerpts','image ')


class UpdateArticleView(UpdateView): 
    model = Article  
    form_class = ArticleForm
    template_name = 'base/update_article.html' 
    # fields = '__all__'


class DeleteArticleView(DeleteView):
    model = Article 
    template_name = 'base/delete_article.html'
    success_url = reverse_lazy('home')


# templates
    


   


def AimAndScopeview(request): 
    return render(request, 'base/Aims_scope.html') 



def HistoryOfTheJournalview(request): 
    return render(request, 'base/history.html') 




def GuidlinesForAuthorsview(request): 
    return render(request, 'base/Guidelines.html')





def EditorialTeamView(request): 
    return render(request, 'base/editorial_team.html') 




def CurrentIssuesView(request):
    return render(request, 'base/current_issues.html')




def ArchivesView(request):
    return render(request, 'base/archives.html')




def AnnouncementView(request):
    return render(request, 'base/announce.html')




def ConferencesView(request):
    return render(request, 'base/confercences.html')





def IndexingView(request):
    return render(request, 'base/indexing.html')




def ContactUsView(request):
    return render(request, 'base/contact_us.html')




def InPressView(request):
    return render(request, 'base/inpress.html')




def SpecialEditorsView(request):
    return render(request, 'base/special_editors.html')
     
    


# class HistoryOfTheJournalview( DetailView):  
#     model = Article  
#     template_name = 'base/history_of_journal.html'



# class EditorialTeamView( DetailView):  
#     model = Article  
#     template_name = 'base/editorial_team.html'



# class GuidelinesForAuthorsView( DetailView):  
#     model = Article  
#     template_name = 'base/guide_lines.html'



# class CurrentIssuesView( DetailView):  
#     model = Article  
#     template_name = 'base/current_issues.html'



# class ArchivesView( DetailView):  
#     model = Article  
#     template_name = 'base/archives.html'



# class AnnouncementView( DetailView):  
#     model = Article  
#     template_name = 'base/Announcement.html'



# class ConferencesView( DetailView):  
#     model = Article  
#     template_name = 'base/Conferences.html'




# class IndexingView( DetailView):  
#     model = Article  
#     template_name = 'base/Indexing.html'


# class ContactUsView( DetailView):  
#     model = Article  
#     template_name = 'base/ContactUs.html'


# class InPressView( DetailView):  
#     model = Article  
#     template_name = 'base/InPress.html'


# class SpecialEditorsView( DetailView):  
#     model = Article  
#     template_name = 'base/SpecialEditors.html'                

    




def Search(request):
    q = request.GET.get('q', '') 


    articles = Article.objects.filter(
       Q(name_of_corresponding_author__icontains=q)|
       Q(main_text__icontains=q)|
       Q(title__icontains=q)
       ).filter(published=True)
    context = { 'articles':articles, 'q':q }
    return render(request, 'base/search.html', context)

   

    
    


# def aims_ang_scope(request):
#     return render(request, 'base/Aims_scope.html')