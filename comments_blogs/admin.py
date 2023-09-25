from django.contrib import admin

from .models import CommentBlog


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['owner', 'blog', 'content', 'created_at']
    search_fields = ['owner', 'blog', 'content']
    list_filter = ['created_at']

    def __str__(self):
        return f'{self.title}'

admin.site.register(CommentBlog, BlogCommentAdmin)