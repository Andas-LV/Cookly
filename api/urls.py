from .views import users_views, recipes_views, products_views
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path, re_path

urlpatterns = [
    path('', users_views.index, name='index'),
    path('register/', users_views.register),
    path('login/', users_views.login),
    path('user/me/', users_views.get_me, name='user-me'),

    path('recipes/', recipes_views.get_all_recipes, name='get_all_recipes'),
    path('products/', products_views.get_all_products, name='get_all_products'),
    path('recipes/<int:recipe_id>/products/', recipes_views.get_recipe_products, name='get_recipe_products'),
    path('products/<int:product_id>/recipes/', products_views.get_recipes_by_product, name='get_recipes_by_product'),

    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('user/update-avatar/', users_views.update_avatar, name='update-avatar'),
    path('recipes/<int:id>/upload-image/', recipes_views.update_recipe_image, name='recipe-upload-image'),
    path('products/<int:id>/upload-image/', products_views.update_product_image, name='product-upload-image'),
]