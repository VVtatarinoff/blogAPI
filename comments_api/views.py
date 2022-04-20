from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from mptt.utils import get_cached_trees
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
    NOT_NUMBER_ERROR = {"error": {"code": 3, "msg": "параметр должен быть числом"}}
    serializer_class = CommentViewSerializer

    queryset = Comments.objects.root_nodes()

    def get(self, request):
        if article := request.query_params.get('article', None):
            try:
                article = int(article)
            except ValueError:
                return Response(self.NOT_NUMBER_ERROR, status=400)
            comments = Comments.objects.filter(article=article, level__lt=3)
        elif parent := request.query_params.get('parent', None):
            try:
                parent = int(parent)
            except ValueError:
                return Response(self.NOT_NUMBER_ERROR, status=400)
            try:
                parent_node = Comments.objects.get(id=parent)
            except ObjectDoesNotExist:
                return Response({"error": {"code": 4, "msg": "нет такой записи"}}, status=404)
            comments = parent_node.get_descendants()
        else:

            return Response({"error": {"code": 3, "msg": "нужно указать либо article либо parent"}}, status=400)
        data = []
        tree = get_cached_trees(queryset=comments.all())
        for node in tree:
            data.append(self.serializable_object(node))
        return Response(data)

    def serializable_object(self, node):
        "Рекурсивно проходит с головы дерева для создания вложенного словаря"
        obj = {'name': node.name, 'id': node.pk, "text":node.text, "left":node.lft, 'right': node.rght,'tree': node.tree_id,'children': []}
        for child in node.get_children():
            obj['children'].append(self.serializable_object(child))
        return obj
