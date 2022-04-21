from django.contrib import admin
from mptt.admin import MPTTModelAdmin

# Register your models here.
from articles.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body')

admin.site.register(Article, ArticleAdmin)

