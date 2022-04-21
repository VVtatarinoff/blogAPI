from django.contrib import admin

from django.urls import path
from comments import views

urlpatterns = [
    path("comment/", views.CommentView.as_view()),

]