from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='images/')
    img_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(200, 150)],
        format='JPEG',
        options={
            'quality': 90,
        },
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
