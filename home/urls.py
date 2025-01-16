from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('review/', views.create_review, name='create_review'),
]
