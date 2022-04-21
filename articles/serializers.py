from rest_framework import serializers

from articles.models import Article


class ArticleCreateSerializer(serializers.ModelSerializer):
    """Добавление комментария"""

    class Meta:
        model = Article
        fields = "__all__"
