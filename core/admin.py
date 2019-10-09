from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', 'preview')


@admin.register(models.Story)
class StoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', 'preview')
