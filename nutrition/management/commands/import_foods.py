import csv
import os
from django.core.management.base import BaseCommand
from nutrition.models import FoodItem

class Command(BaseCommand):
    help = 'Import food items from a CSV file'

    def handle(self, *args, **kwargs):
        file_path = os.path.join('nutrition', 'data', 'food_items_english.csv')

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            added, skipped = 0, 0

            for row in reader:
                name = row['name']
                calories = int(row['calories'])
                proteins = float(row['proteins'])
                fats = float(row['fats'])
                carbs = float(row['carbs'])

                obj, created = FoodItem.objects.get_or_create(
                    name=name,
                    defaults={
                        'calories': calories,
                        'proteins': proteins,
                        'fats': fats,
                        'carbs': carbs,
                    }
                )
                if created:
                    added += 1
                else:
                    skipped += 1

            self.stdout.write(self.style.SUCCESS(f"Imported: {added}, Skipped (duplicates): {skipped}"))
