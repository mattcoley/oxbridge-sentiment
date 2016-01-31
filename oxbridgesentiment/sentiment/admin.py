from django.contrib import admin
from .models import TweetGroup

class TweetAdmin(admin.ModelAdmin):
    list_display = ['date_added', 'name', 'positive', 'negative', 'sentiment']
    ordering = ['date_added', 'name', 'positive', 'negative']
    search_fields = ['name', 'date']

admin.site.register(TweetGroup, TweetAdmin)
