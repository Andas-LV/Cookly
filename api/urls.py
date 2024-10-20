from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', index, name='index'),
    path('register/', register),
    path('login/', login),
    path('user/me/', get_me, name='user-me'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/update-avatar/', update_avatar, name='update-avatar'),
]