from django.urls import path
from . import views


app_name = 'teachers'

urlpatterns = [

    path('tasks/', views.tasks, name='tasks'),

]