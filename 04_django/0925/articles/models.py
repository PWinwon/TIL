from django.db import models
from imagekit import processors
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    upload = models.FileField(upload_to='images/', blank=True)
    image = ProcessedImageField(
        blank=True,
        processors=[Thumbnail(200, 300)],
        format='JPEG',
        options={'quality': 90},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)