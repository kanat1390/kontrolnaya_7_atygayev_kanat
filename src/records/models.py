from random import choices
from django.db import models
from .managers import RecordManager

STATUS_CHOICES = (
    ('active', 'Активно'), 
    ('blocked', 'Заблокировано'), 
)



class Record(models.Model):
    author = models.CharField(null=False, blank=False, max_length=100)
    email = models.EmailField(null=False, blank=False, max_length=100)
    body = models.TextField(null=False, blank=False, max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=7, default=STATUS_CHOICES[0][0])
    objects = RecordManager()

    def __str__(self):
        return f'{self.author}-{self.created_at}'


