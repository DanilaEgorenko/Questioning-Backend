from django.contrib import admin
from .models import Questions


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "body")
    list_filter = (
        "author",
    )
    search_fields = ("title__startswith", )


admin.site.register(Questions, QuestionsAdmin)
