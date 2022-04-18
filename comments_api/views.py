from rest_framework.response import Response
from rest_framework.views import APIView

from comments_api.serializers import ArticleCreateSerializer


class ArticleCreateView(APIView):
    """Добавление отзыва к фильму"""
    def post(self, request):
        article = ArticleCreateSerializer(data=request.data)
        if article.is_valid():
            article.save()
        return Response(status=201)
