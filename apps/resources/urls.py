from django.urls import path
from . import views

app_name = 'resources'  # Add this line

urlpatterns = [
    path('', views.resources, name='resources'),
    path('<slug:slug>/', views.resource_detail, name='resource_detail'),
]