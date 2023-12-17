from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        # Очищаем таблицы перед заполнением
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Заполняем категории
        electronics_category = Category.objects.create(name='Electronics', description='Electronic gadgets')
        clothing_category = Category.objects.create(name='Clothing', description='Fashion and clothing')
        books_category = Category.objects.create(name='Books', description='Various books')

        # Заполняем продукты
        Product.objects.create(name='Laptop', description='High-performance laptop', category=electronics_category,
                               price=10000)
        Product.objects.create(name='Smartphone', description='Latest smartphone model', category=electronics_category,
                               price=1000)
        Product.objects.create(name='T-shirt', description='Comfortable cotton T-shirt', category=clothing_category,
                               price=300)
        Product.objects.create(name='Jeans', description='Classic blue jeans', category=clothing_category, price=600)
        Product.objects.create(name='Sci-Fi Book', description='Exciting science fiction novel',
                               category=books_category, price=150)
        Product.objects.create(name='Cookbook', description='Collection of delicious recipes', category=books_category,
                               price=200)

        self.stdout.write(self.style.SUCCESS('Data successfully populated'))
