from storages.backends.s3boto3 import S3Boto3Storage
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, storage=S3Boto3Storage())

    def __str__(self):
        return self.user.username