from django.contrib import admin

from django.urls import path
from comments import views

urlpatterns_comments = [
    path("/", views.CommentView.as_view()),

]