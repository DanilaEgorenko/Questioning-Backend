from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index),
    # path("<int:page>", views.index),
    path("", views.QuestionsViewSet.as_view({"get": "list"})),
    path("<int:page>", views.QuestionsViewSet.as_view({"get": "list"})),
    path("profile", views.ProfileViewSet.as_view({"get": "list"})),
    path("delete/<int:id>/", views.ProfileViewSet.as_view({"post": "delete"})),
    path("create", views.create),
    path("question/<int:id>/", views.question, name="question"),
    path("edit/<int:id>/", views.edit),
]
