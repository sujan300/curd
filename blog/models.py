from django.db import models

# Create your models here.
class Post(models.Model):
    title     = models.CharField(max_length=225)
    content   = models.TextField()
    photo     = models.ImageField(upload_to="photo")

    def __str__(self):
        return self.title