from storages.backends.s3boto3 import S3Boto3Storage
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, storage=S3Boto3Storage)

    def __str__(self):
        return self.user.username

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/', null=True, blank=True, storage=S3Boto3Storage)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    products = models.ManyToManyField(Product, related_name='recipes')
    image = models.ImageField(upload_to='recipes/', null=True, blank=True, storage=S3Boto3Storage)

    class Meta:
        db_table = 'recipes'

    def __str__(self):
        return self.name
