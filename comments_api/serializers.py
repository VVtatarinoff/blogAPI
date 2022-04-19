from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from comments_api.models import Comments, Article


class RecursiveSerializer(serializers.Serializer):
    """Вывод рекурсивно children"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Добавление комментария"""

    class Meta:
        model = Comments
        fields = "__all__"


class ArticleCreateSerializer(serializers.ModelSerializer):
    """Добавление комментария"""

    class Meta:
        model = Article
        fields = "__all__"


class FilterCommentListSerializer(serializers.ListSerializer):
    """Фильтр комментариев, только parents"""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class CommentViewSerializer(serializers.ModelSerializer):
    """Вывод комментариев"""
    # children = RecursiveSerializer(many=True)
    # children = SerializerMethodField(source='get_children')

    class Meta:
        # list_serializer_class = FilterCommentListSerializer
        model = Comments
        fields = ("id", "name", "text", "children")

    # def get_children(self, obj):
    #     children = self.context['children'].get(obj.id, [])
    #     serializer = CommentViewSerializer(children, many=True, context=self.context)
    #     return serializer.data
