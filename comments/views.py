from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.response import Response
from mptt.utils import get_cached_trees
from rest_framework.views import APIView

from comments.models import Comments
from comments.serializers import CommentViewSerializer


def serializable_object(node):
    "Рекурсивно проходит с головы дерева для создания вложенного словаря"

    obj = {'name': node.name, 'id': node.pk, "text": node.text, "left": node.lft, 'right': node.rght,
           'tree': node.tree_id, 'children': []}
    for child in node.get_children():
        obj['children'].append(serializable_object(child))
    return obj


def get_tree(query):
    data = []
    tree = get_cached_trees(queryset=query.all())
    for node in tree:
        data.append(serializable_object(node))
    return data


class ArticleCommentView(APIView):

    def get(self, request, pk):
        comments = Comments.objects.filter(article=pk, level__lt=3)
        return Response(get_tree(comments))


class CommentsToCommentView(GenericAPIView):
    serializer_class = CommentViewSerializer

    queryset = Comments.objects.all()

    def get(self, request, pk):
        try:
            parent_node = Comments.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response({"error": {"code": 4, "msg": "нет такой записи"}}, status=404)
        comments = parent_node.get_descendants()
        return Response(get_tree(comments))


class AddCommentView(APIView):

    def post(self, request):
        comment = CommentViewSerializer(data=request.data)
        if comment.is_valid():
            try:
                comment.save()
            except Exception as e:
                return Response({"error": {"code": 1, "msg": "ошибка записи в БД"}}, status=400)
            return Response(status=201)
        return Response({"error": {"code": 2, "msg": comment.errors}}, status=400)
