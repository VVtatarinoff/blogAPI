from django.contrib import admin
from mptt.admin import MPTTModelAdmin

# Register your models here.
from comments_api.models import Article, Comments


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body')


class CommentsAdmin(MPTTModelAdmin):
    list_display = ('id', 'name', 'text', 'parent', 'article', 'level')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comments, CommentsAdmin)
