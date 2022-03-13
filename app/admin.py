from csv import list_dialects
from django.contrib import admin
from app.models import Article, Member


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at')



admin.site.register(Article, ArticleAdmin)
admin.site.register(Member)