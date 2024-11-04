from celery import shared_task
from .models import Profile
import boto3
from django.conf import settings

@shared_task
def update_avatar_task(user_id, avatar_file_path):
    s3 = boto3.client('s3')

    try:
        profile = Profile.objects.get(user_id=user_id)
        avatar_file_name = f'{user_id}_avatar.jpg'
        s3.upload_file(avatar_file_path, settings.AWS_STORAGE_BUCKET_NAME, avatar_file_name)

        profile.avatar.name = avatar_file_name
        profile.save()
    except Profile.DoesNotExist:
        return {'error': 'User profile does not exist.'}
