from django.contrib import admin
from .models import Questions
from .models import Review
from .models import User
from .models import PremiumUser
from .models import Notifications
from .models import EmailReceivers
from import_export.admin import ExportActionMixin
from simple_history.admin import SimpleHistoryAdmin


class QuestionsAdmin(ExportActionMixin, SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ("title", "author", "body")
    list_filter = (
        "title",
        "author",
    )
    search_fields = (
        "title__startswith",
        "author__startswith",
    )


class ReviewAdmin(ExportActionMixin, SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ("questionID", "textReview")
    search_fields = (
        "questionID__startswith",
        "textReview__startswith",
    )


class UserAdmin(ExportActionMixin, SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ("id", "username", "email")
    list_filter = ("id", "username", "email")
    search_fields = ("id__startswith", "username__startswith", "email__startswith")


class PremiumUserAdmin(ExportActionMixin, SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ("id", "level")
    list_filter = ("id", "level")
    search_fields = ("id__startswith", "level__startswith")


class NotificationsAdmin(ExportActionMixin, SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ("title", "receiverID", "textNotification")
    list_filter = ("title", "receiverID", "textNotification")
    search_fields = ("title__startswith", "textNotification__startswith")


class EmailReceiversAdmin(ExportActionMixin, SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ("id", "date_subscribe")
    list_filter = ("id", "date_subscribe")
    search_fields = ("id__startswith", "date_subscribe__startswith")


admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(PremiumUser, PremiumUserAdmin)
admin.site.register(Notifications, NotificationsAdmin)
admin.site.register(EmailReceivers, EmailReceiversAdmin)
