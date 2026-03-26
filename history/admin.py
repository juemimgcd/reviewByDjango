from django.contrib import admin

from .models import History


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "news", "view_time"]
    list_filter = ["view_time"]
    search_fields = ["user__username", "news__title"]
