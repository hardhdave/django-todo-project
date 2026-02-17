from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name ='todo_list'),
    path('add/', views.add_todo, name='add_todo'),
    path('edit/<int:id>/', views.edit_todo, name='edit_todo'),
    path('complete/<int:id>/', views.mark_complete, name='mark_complete'),
    path('delete/<int:id>/', views.delete_todo, name ='delete_todo'),
]
