from django.urls import path
from . import views

urlpatterns = [
    # Read
    path('', views.profiles, name='profile_list'),
    #Create
    path('create/', views.profile_create, name='profile_create'),
    #Update
    path('update/<int:pk>/', views.profile_update, name='profile_update'),
    #Delete
    path('delete/<int:pk>/', views.profile_delete, name='profile_delete'),
]
