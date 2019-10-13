from django.contrib import admin
from . import models


@admin.register(models.CribbagePost)
class CribbageAdmin(admin.ModelAdmin):
    readonly_fields = ('preview',)
