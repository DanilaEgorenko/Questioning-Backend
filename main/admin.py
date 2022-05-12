from django.contrib import admin
from .models import Questions


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "body")


admin.site.register(Questions, QuestionsAdmin)
