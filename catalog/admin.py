from django.contrib import admin
from .models import Category, Product


# Регистрация модели Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')  # Отображаемые поля в списке


# Регистрация модели Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'description')  # Отображаемые поля в списке
    list_filter = ('category',)  # Добавление фильтрации по категории
    search_fields = ('name', 'description')  # Добавление возможности поиска по названию и описанию
