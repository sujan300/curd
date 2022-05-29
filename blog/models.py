from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    title     = models.CharField(max_length=225)
    content   = models.TextField()
    photo     = CloudinaryField('image')

    def __str__(self):
        return self.title