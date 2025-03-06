from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(default=timezone.now)


class Features(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} - {self.subject}"