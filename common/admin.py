from django.contrib import admin
from common.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('text', 'to_book', 'updated_at',)
    search_fields = ('user',)
    ordering = ('updated_at',)
