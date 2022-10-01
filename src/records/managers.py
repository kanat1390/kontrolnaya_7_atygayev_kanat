from django.db import models

class RecordManager(models.Manager):

    def set_queryset(self):
        return super().get_queryset()
    
    def active(self):
        return self.set_queryset().filter(status='active').order_by('-created_at')