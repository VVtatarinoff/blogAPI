from rest_framework import serializers

from comments.models import Comments


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Добавление комментария"""

    class Meta:
        model = Comments
        fields = "__all__"


class FilterCommentListSerializer(serializers.ListSerializer):
    """Фильтр комментариев, только parents"""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class CommentViewSerializer(serializers.ModelSerializer):
    """Вывод комментариев"""

    class Meta:
        model = Comments
        fields = ("name", "text")