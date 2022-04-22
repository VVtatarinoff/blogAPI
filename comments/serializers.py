from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from comments.models import Comments


class ReviewSerializer(serializers.ModelSerializer):
    """Вывод комментариев"""

    class Meta:
        model = Comments
        fields = ("name", "text", "article", "children")


class CommentViewSerializer(serializers.ModelSerializer):
    """Добавление комментария"""

    def validate(self, attrs):
        parent = attrs.get('parent')
        article = attrs.get('article')

        if parent and article and parent.article_id != article.id:
            raise ValidationError(detail="Article не совпадает с article родителя")
        return super().validate(attrs)

    class Meta:
        model = Comments
        fields = ("name", "text", "article", "parent")
