from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='', blank=True, upload_to = 'images')

    def __str__(self):
        return self.title

