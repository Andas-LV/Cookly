from .views import *
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('register/', register),
    path('login/', login),
    path('user/me/', get_me, name='user-me'),

    path('recipes/', get_all_recipes, name='get_all_recipes'),
    path('products/', get_all_products, name='get_all_products'),
    path('recipes/<int:recipe_id>/products/', get_recipe_products, name='get_recipe_products'),

    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('user/update-avatar/', update_avatar, name='update-avatar'),
    path('recipes/<int:id>/upload-image/', update_recipe_image, name='recipe-upload-image'),
    path('products/<int:id>/upload-image/', update_product_image, name='product-upload-image'),
]