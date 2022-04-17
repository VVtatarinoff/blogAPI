from django.db import models


# Create your models here.

class Article(models.Model):
    """статья"""
    title = models.CharField("Название", max_length=100)
    body = models.TextField("Текст статьи")

    def __str__(self):
        return self.title

    def get_comment(self):
        return self.comments_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Comments(models.Model):
    """Комментарии"""
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Комментарий", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True,
        null=True, related_name="children"
    )
    article = models.ForeignKey(Article, verbose_name="статья", on_delete=models.CASCADE,
                                related_name="comments")

    def __str__(self):
        return f"{self.name} - {self.article}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
