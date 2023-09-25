from django.contrib import admin

from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'created_at', 'updated_at']
    search_fields = ['title', 'owner', 'blogs']
    list_filter = ['created_at']

    def __str__(self):
        return f'{self.title}'

admin.site.register(Blog, BlogAdmin)
