from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('view/', views.view, name='view')

]