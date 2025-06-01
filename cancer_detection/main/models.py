from django.db import models
from django.utils import timezone

class Detection(models.Model):
    image = models.ImageField(upload_to='detections/')
    result = models.TextField(blank=True, null=True)
    confidence = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"Detection {self.id} - {self.created_at.strftime('%Y-%m-%d %H:%M')}" 