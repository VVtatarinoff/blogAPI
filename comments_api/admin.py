from django.contrib import admin

# Register your models here.
from comments_api.models import Article, Comments


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body')


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'parent', 'article')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comments, CommentsAdmin)
