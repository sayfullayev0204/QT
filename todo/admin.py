from django.contrib import admin
from .models import Article, Image

class ImageInline(admin.TabularInline):
    model = Image

class ArticleAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Article, ArticleAdmin)