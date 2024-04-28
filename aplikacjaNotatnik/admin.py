from django.contrib import admin
from .models import Note


# Register your models here.
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'status', 'author', 'time']
    list_filter = ['title', 'status']
    date_hierarchy = 'time'
    search_fields = ['title', 'text']
    ordering = ['status', 'time']


