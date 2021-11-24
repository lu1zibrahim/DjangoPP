from django.contrib.admin import ModelAdmin, register  # noqa
from django.contrib import admin

from aperitivos.models import Video


@register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'creation', 'vimeo_id')
    ordering = ('creation',)
    prepopulated_fields = {"slug": ("titulo",)}
