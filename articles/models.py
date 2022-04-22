from django.db import models


# Create your models here.
class Article(models.Model):
    """статья"""
    title = models.CharField("Название", max_length=100, unique=True)
    body = models.TextField("Текст статьи")

    def __str__(self):
        return self.title

    def get_comment(self):
        return self.comments_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
