from celery import shared_task
from django.contrib.auth.models import User

@shared_task
def update_avatar_task(user_id, avatar_data):
    try:
        user = User.objects.get(id=user_id)
        profile = user.profile
        profile.avatar.save(avatar_data.name, avatar_data)
        profile.save()
        return {'status': 'success', 'avatar_url': profile.avatar.url}
    except User.DoesNotExist:
        return {'status': 'error', 'message': 'User does not exist'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}
