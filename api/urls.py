from .views import users_views, recipes_views, products_views
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path

urlpatterns = [
    path('', users_views.index, name='index'),
    # AUTH
    path('register/', users_views.register),
    path('login/', users_views.login),
    path('user/me/', users_views.get_me, name='user-me'),
    # GENERAL
    path('recipes/', recipes_views.get_all_recipes, name='get_all_recipes'),
    path('products/', products_views.get_all_products, name='get_all_products'),
    # FILTERED RECIPES
    path('getHealthyRecipes/', recipes_views.get_healthy_recipes, name='get_all_recipes'),
    path('getBreakfastRecipes/', recipes_views.get_breakfast_recipes, name='get_all_recipes'),
    path('getLunchRecipes/', recipes_views.get_lunch_recipes, name='get_all_recipes'),
    path('getDinnerRecipes/', recipes_views.get_dinner_recipes, name='get_all_recipes'),
    path('getPopularRecipes/', recipes_views.get_popular_recipes, name='get_all_recipes'),
    # BY ID
    path('recipes/<int:recipe_id>/products/', recipes_views.get_recipe_products, name='get_recipe_products'),
    path('products/<int:product_id>/recipes/', products_views.get_recipes_by_product, name='get_recipes_by_product'),
    # AVATARS & UTILS
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('user/update-avatar/', users_views.update_avatar, name='update-avatar'),
    path('recipes/<int:id>/upload-image/', recipes_views.update_recipe_image, name='recipe-upload-image'),
    path('products/<int:id>/upload-image/', products_views.update_product_image, name='product-upload-image'),
]