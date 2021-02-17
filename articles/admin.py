from django.contrib import admin
from .models import Article, Comment


class CommentInline(admin.TabularInline): # admin.StackedInline(StackedInline view)
    model = Comment
    extra = 2


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)