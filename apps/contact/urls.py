from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('newsletter/', views.newsletter_signup, name='newsletter_signup'),
]