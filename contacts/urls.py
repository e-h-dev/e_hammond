from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.contacts, name='contacts'),
    path('sent/', views.sent_messages, name='sent_messages'),
    path('compose/', views.compose_message, name='compose_message'),
    path('<int:contact_id>', views.open_message, name='open_message'),
    path('<int:contact_id>/unread', views.mark_unread, name='mark_unread'),
    path('reply_message/<int:contact_id>', views.reply_message, name='reply_message'),
    path('delete/<int:contact_id>/',
         views.delete_message, name='delete_message'),
]
