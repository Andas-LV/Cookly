from .views import users_views, recipes_views, ingredients_views
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path

urlpatterns = [
    path('', users_views.index, name='index'),
    # AUTH
    path('register/', users_views.register),
    path('login/', users_views.login),
    path('user/me/', users_views.get_me, name='user-me'),
    # GENERAL
    path('recipes/category/<str:category>/', recipes_views.get_recipes_by_category, name='get_recipes_by_category'),
    path('ingredients/', ingredients_views.get_all_ingredients, name='get_all_products'),

    # FAVOURITE & BASKET
    path('ingredients/<int:ingredient_id>/favourite/', ingredients_views.toggle_favourite, name='toggle_favourite'),
    path('ingredients/<int:ingredient_id>/basket/', ingredients_views.toggle_basket, name='toggle_basket'),
    path('recipes/<int:recipe_id>/favourite/', recipes_views.toggle_recipe_favourite, name='toggle_recipe_favourite'),
    path('recipes/<int:recipe_id>/basket/', recipes_views.toggle_recipe_basket, name='toggle_recipe_basket'),
    # BY ID
    path('recipes/<int:recipe_id>/', recipes_views.get_recipe_by_id, name='get_recipe_products'),
    path('ingredients/<int:ingredient_id>/', ingredients_views.get_ingredient_by_id, name='get_ingredient_by_id'),
    # AVATARS & UTILS
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('user/update-avatar/', users_views.update_avatar, name='update-avatar'),
]