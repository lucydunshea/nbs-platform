from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('projects/', views.projects_index, name='projects_index'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('articles/', views.articles_index, name='articles_index'),
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),
    path('about/', views.about_page, name='about_page'),
    path('contact/', views.contact_page, name='contact_page'),
]