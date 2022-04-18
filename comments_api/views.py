from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from comments_api.models import Comments
from comments_api.serializers import ArticleCreateSerializer, CommentViewSerializer


class ArticleCreateView(APIView):
    """Добавление статьи"""

    def post(self, request):
        article = ArticleCreateSerializer(data=request.data)
        if article.is_valid():
            try:
                article.save()
            except Exception:
                return Response({"error": {"code": 1, "msg": "ошибка записи в БД"}}, status=400)
            return Response(status=201)
        return Response({"error": {"code": 2, "msg": article.errors['title']}}, status=400)


class CommentView(GenericAPIView):
    """Добавление комментария к статье"""
    NOT_NUMBER_ERROR = {"error": {"code":3, "msg":"параметр должен быть числом"}}
    serializer_class = CommentViewSerializer
    def get_queryset(self):
        pass

    def get(self, request):
        if article := request.query_params.get('article', None):
            try:
                article = int(article)
            except ValueError:
                return Response(self.NOT_NUMBER_ERROR, status=400)
            comments = Comments.objects.filter(article=article, parent=None)
            data = []
            for n in comments:
                data.append(self.recursive_node_to_dict(n))

            return Response(data)
            #serializer = CommentViewSerializer(comments, many=True)
            #return Response(serializer.data)
        elif parent := request.query_params.get('parent', None):
            try:
                parent = int(article)
            except ValueError:
                return Response(self.NOT_NUMBER_ERROR, status=400)

        return Response({"error": {"code":3, "msg":"нужно указать либо article либо parent"}}, status=400)

    def recursive_node_to_dict(self, node, level=2):
        if node.level == level:
            return
        result = self.get_serializer(instance=node).data
        children = [self.recursive_node_to_dict(c) for c in node.get_children()]
        if children:
            result["children"] = children
        return result
