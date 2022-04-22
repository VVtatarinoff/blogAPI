from django.urls import path
from comments import views

urlpatterns_comments = [
    path("article/<int:pk>", views.ArticleCommentView.as_view()),
    path("parent/<int:pk>", views.CommentsToCommentView.as_view()),
    path("add", views.AddCommentView.as_view())
]
