from django.contrib import admin

from .models import Journey


class JourneyAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'created_at', 'updated_at']
    search_fields = ['title', 'owner', 'created_at']
    list_filter = ['created_at']

    def __str__(self):
        return f'{self.title}'

admin.site.register(Journey, JourneyAdmin)