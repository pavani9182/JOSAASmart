

import csv
from django.core.management.base import BaseCommand
from josaa_app.models import josaa 

class Command(BaseCommand):
    help = 'Import CSV data into josaa model'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file to be imported')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Skip the header row
            


            for row in reader:
                josaa.objects.create(
                    Institute=row[0],
                    Academic_Program_Name=row[1],
                    Seat_Type=row[2],
                    Gender=row[3],
                    Opening_Rank=row[4],
                    Closing_Rank=row[5],
                    year=row[6],
                    round=row[7],
                )

        #"python manage.py import_csv path_to_csv_file" -command helps to import data stored from csv file and creates objects in josaa module

        self.stdout.write(self.style.SUCCESS(f'Successfully imported data from {csv_file}'))


