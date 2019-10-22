from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from . import models


class CommentInline(GenericTabularInline):
    model = models.Comment
    extra = 1


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('preview',)
    inlines = (CommentInline,)


@admin.register(models.HTMLPost)
class HTMLPostAdmin(admin.ModelAdmin):
    readonly_fields = ('preview',)
    inlines = (CommentInline,)
