from django.contrib import admin

from .models import Responses


class ResponseAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "id",
        "user",
        "article",
        "parent_responses",
        "content",
        "created_at",
    ]
    list_display_links = ["pkid", "id", "user"]


# Register your models here.
admin.site.register(Responses, ResponseAdmin)
