from rest_framework.response import Response
from rest_framework.views import APIView
from articles.serializers import ArticleCreateSerializer


# Create your views here.

class ArticleCreateView(APIView):
    """Добавление статьи"""

    def post(self, request):
        article = ArticleCreateSerializer(data=request.data)
        if article.is_valid():
            try:
                article.save()
            except Exception:
                return Response({"error": {"code": 1,
                                           "msg": "ошибка записи в БД"}},
                                status=400)
            return Response(status=201)
        return Response({"error": {"code": 2,
                                   "msg": article.errors['title']}},
                        status=400)
