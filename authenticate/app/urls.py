from django.urls import path
from . import views

urlpatterns = [
    path('', views.authenticate, name='authenticate'),
    path('success/', views.success, name='success'),
    path('error/', views.error, name='error')


    
]