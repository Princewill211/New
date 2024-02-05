from django.urls import path
from . import views
from .views import  HomeView,ArticleDetailView,AddArticleView,UpdateArticleView,DeleteArticleView







urlpatterns = [

    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_article/', AddArticleView.as_view(), name='add_article' ),
    path('article/edit/<int:pk>', UpdateArticleView.as_view(), name="update_article"),
    path('article/<int:pk>/remove', DeleteArticleView.as_view(), name="delete_article"),
    path('Aims/', views.AimAndScopeview, name='Aims_scope'),
    path('search/', views.Search, name='search'),
    path('history/', views.HistoryOfTheJournalview, name='history-journal'),
    path('editorial_team/', views.EditorialTeamView, name='editorial_team'),
    path('guide_lines/',  views.GuidlinesForAuthorsview, name='guide-lines'),
    path('current_issues/', views.CurrentIssuesView, name='current_issues'),
    path('archives/', views.ArchivesView, name='archives'),
    path('Announcement/',  views.AnnouncementView, name='Announcement'),
    path('Conferences/', views.ConferencesView, name='Conferences'),
    path('Indexing/', views.IndexingView, name='Indexing'),
    path('ContactUs/', views.ContactUsView, name='ContactUs'),
    path('InPress/', views.InPressView, name='InPress'),
    path('SpecialEditors/', views.SpecialEditorsView, name='SpecialEditors'),

    # path('login/', views.loginPage, name="login"),
    # path('logout/', views.logoutUser, name="logout"),
    # path('register/', views.registerPage, name="register"),
    # path('aims-scope/', views.aims_ang_scope, name="aims_ang_scope"),
]