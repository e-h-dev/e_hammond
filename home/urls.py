from django.urls import path, include
from . import views
from contacts import views as contact_views

urlpatterns = [
    path('', views.index, name='home'),
    path('review/', views.create_review, name='create_review'),
    path('compose/', contact_views.compose_message, name='compose_message'),
]
