from rest_framework.generics import CreateAPIView

from articles.models import Article
from articles.serializers import ArticleCreateSerializer


class ArticleCreateView(CreateAPIView):
    """Добавление статьи"""
    serializer_class = ArticleCreateSerializer
    queryset = Article.objects.all()
