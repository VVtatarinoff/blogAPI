from rest_framework import serializers

from comments.models import Comments


class ReviewSerializer(serializers.ModelSerializer):
    """Добавление комментария"""

    class Meta:
        model = Comments
        fields = ("name", "text", "article", "children")


class CommentViewSerializer(serializers.ModelSerializer):
    """Вывод комментариев"""

    def is_valid(self, raise_exception=False):
        validation = super().is_valid()
        parent = self.validated_data.get('parent')
        if parent and validation:
            if parent.article_id != self.validated_data.get('article').id:
                validation = False
                self._errors[
                    'Not matching'] = "Article не совпадает с article родителя"
        return validation

    class Meta:
        model = Comments
        fields = ("name", "text", "article", "parent")
