from django.urls import path
from . import views

urlpatterns = [
    path('', views.our_work, name='our_work'),
    path('<slug:slug>/', views.work_category_detail, name='work_category_detail'),
]