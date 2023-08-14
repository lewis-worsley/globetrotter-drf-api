from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    search_fields = ['title']
    list_filter = ['created_at']

    def __str__(self):
        return f'{self.title}'

admin.site.register(News, NewsAdmin)