from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    """ Massage Admin Definition """

    list_display = (
        "__str__",
        "created",
    )


@admin.register(models.Conversation)
class ConversationsAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "count_massages",
        "count_participants",
    )
