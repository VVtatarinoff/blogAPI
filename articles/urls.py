from django.contrib import admin

from django.urls import path
from articles import views

urlpatterns_article = [
    path("/", views.ArticleCreateView.as_view()),
]
