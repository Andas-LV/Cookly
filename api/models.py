from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.CharField(null=True, blank=True)
    price = models.IntegerField(default=0)
    is_favourite = models.BooleanField(default=False)
    in_basket = models.BooleanField(default=False)

    class Meta:
        db_table = 'ingredients'

    def __str__(self):
        return self.name

class Recipes(models.Model):
    CATEGORY_CHOICES = [
        ('breakfast', 'Завтрак'),
        ('lunch', 'Обед'),
        ('dinner', 'Ужин'),
        ('salad', 'Салат'),
        ('dessert', 'Десерт'),
    ]
    COOKING_LEVEL_CHOICES = [
        ('easy', 'Легкая'),
        ('medium', 'Средняя'),
        ('hard', 'Сложная'),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    cooking_time = models.PositiveIntegerField(
        help_text="Время приготовления в минутах",
        default=30
    )
    calories = models.PositiveIntegerField(
        help_text="Калорийность",
        default=200
    )
    cooking_level = models.CharField(max_length=10, choices=COOKING_LEVEL_CHOICES)
    description = models.TextField()
    preparation = models.TextField(help_text="Шаги приготовления")
    image = models.CharField(max_length=100)
    is_favourite = models.BooleanField(default=False)
    in_basket = models.BooleanField(default=False)

    class Meta:
        db_table = 'recipes'

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name='ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.CharField(max_length=50, help_text="Количество (граммы, штуки и т.д.)")

    class Meta:
        db_table = 'recipe_products'
        unique_together = ('recipe', 'ingredient')

    def __str__(self):
        return f"{self.amount} {self.ingredient.name} для {self.recipe.name}"
