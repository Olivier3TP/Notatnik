import uuid

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Note(models.Model):
    STATUS_CHOICES = (
        ('Important', 'Important'),
        ('Usually', 'Usually')
    )

    title = models.CharField(max_length=100)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Usually')
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_note', args=[self.id])