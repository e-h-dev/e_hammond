from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.contacts, name='contacts'),
    path('<int:contact_id>', views.open_message, name='open_message'),
]
