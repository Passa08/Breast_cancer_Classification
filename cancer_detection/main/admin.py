from django.contrib import admin
from .models import Detection

@admin.register(Detection)
class DetectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'result', 'confidence', 'created_at')
    list_filter = ('created_at', 'result')
    search_fields = ('result',)
    readonly_fields = ('created_at',) 