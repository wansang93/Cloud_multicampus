from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_todo/', views.create_todo, name='create_todo'),
    path('delete_todo/', views.delete_todo, name='delete_todo'),
    path('done_todo/', views.done_todo, name='done_todo'),
]
