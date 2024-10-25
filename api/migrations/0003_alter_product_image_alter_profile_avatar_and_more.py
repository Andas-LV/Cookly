# Generated by Django 5.1.1 on 2024-10-25 13:53

import storages.backends.s3
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_product_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=storages.backends.s3.S3Storage, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, storage=storages.backends.s3.S3Storage, upload_to='avatars/'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=storages.backends.s3.S3Storage, upload_to='recipes/'),
        ),
    ]
