from django.db import models
from django.contrib.auth.models import User
from storages.backends.s3boto3 import S3Boto3Storage

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, storage=S3Boto3Storage())

    def __str__(self):
        return self.user.username

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/', null=True, blank=True, storage=S3Boto3Storage())

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name

class Recipe(models.Model):
    MEAL_TYPE_CHOICES = [
        ('breakfast', 'Завтрак'),
        ('lunch', 'Обед'),
        ('dinner', 'Ужин'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    products = models.ManyToManyField(Product, related_name='recipes')
    image = models.ImageField(upload_to='recipes/', null=True, blank=True, storage=S3Boto3Storage())
    meal_type = models.CharField(max_length=10, choices=MEAL_TYPE_CHOICES, default='breakfast')
    healthy = models.BooleanField(default=True)
    popular = models.BooleanField(default=False)

    class Meta:
        db_table = 'recipes'

    def __str__(self):
        return self.name
