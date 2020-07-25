from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

class Community(models.Model):
    title = models.CharField(max_length=100)

    
    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Community, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})