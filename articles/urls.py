from django.contrib import admin

from django.urls import path, include
from comments import views

urlpatterns = [
    path("article/", views.ArticleCreateView.as_view()),
]
