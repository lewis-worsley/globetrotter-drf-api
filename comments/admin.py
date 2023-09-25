from django.contrib import admin

from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['owner', 'journey', 'content', 'created_at']
    search_fields = ['owner', 'journey', 'content']
    list_filter = ['created_at']

    def __str__(self):
        return f'{self.title}'

admin.site.register(Comment, CommentAdmin)