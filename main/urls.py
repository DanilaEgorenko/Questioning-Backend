from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('profile', views.profile),
    path('create', views.create),
    path('question/<int:id>/', views.question),
    path('delete/<int:id>/', views.delete),
]
