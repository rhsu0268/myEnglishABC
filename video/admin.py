from django.contrib import admin

# Register your models here.
from .models import Video, Note

class NoteInline(admin.StackedInline):
    model = Note

class VideoAdmin(admin.ModelAdmin):
    inlines = [NoteInline,]

admin.site.register(Video)
admin.site.register(Note)


