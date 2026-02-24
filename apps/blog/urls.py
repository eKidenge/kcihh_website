# /home/cs/Desktop/PROJECTS/kcihh_website/apps/blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'  # This sets the namespace

urlpatterns = [
    path('', views.blog_list, name='blog_list'),  # URL name is 'blog_list'
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('category/<slug:category_slug>/', views.blog_category, name='blog_category'),
    path('tag/<slug:tag_slug>/', views.blog_tag, name='blog_tag'),
    path('search/', views.blog_search, name='blog_search'),
]