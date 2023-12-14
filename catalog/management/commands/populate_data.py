from django.core.management.base import BaseCommand
from catalog.models import Category


class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        # Очищаем таблицы перед заполнением
        Category.objects.all().delete()

        # Заполняем данными
        Category.objects.create(name='Electronics', description='Electronic gadgets')
        Category.objects.create(name='Clothing', description='Fashion and clothing')
        Category.objects.create(name='Books', description='Various books')

        self.stdout.write(self.style.SUCCESS('Data successfully populated'))
