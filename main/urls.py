from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('profile', views.profile),
    path('login', views.login),
    path('create', views.create),
    path('question/<int:id>/', views.question),
]
