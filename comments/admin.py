from django.contrib import admin
from mptt.admin import MPTTModelAdmin

# Register your models here.
from comments.models import Comments


class CommentsAdmin(MPTTModelAdmin):
    list_display = ('id', 'name', 'text', 'parent', 'article', 'level')


admin.site.register(Comments, CommentsAdmin)
