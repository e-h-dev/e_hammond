from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.contacts, name='contacts'),
    path('sent/', views.sent_messages, name='sent_messages'),
    path('compose/', views.compose_message, name='compose_message'),
    path('<int:contact_id>', views.open_message, name='open_message'),
    path('unread/<int:contact_id>', views.mark_unread, name='mark_unread'),
    path('delete/<int:contact_id>/',
         views.delete_message, name='delete_message'),
]
