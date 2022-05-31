from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    title     = models.CharField(max_length=225)
    content   = models.TextField()
    photo     = models.ImageField(upload_to ='Image')

    def __str__(self):
        return self.title