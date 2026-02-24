# apps/get_involved/urls.py
from django.urls import path
from . import views

#app_name = 'get_involved'

urlpatterns = [
    path('', views.get_involved, name='index'),  # Make sure this line exists
    path('volunteer/', views.volunteer_application, name='volunteer'),
    path('donate/', views.donate, name='donate'),
    # ... other URLs
]