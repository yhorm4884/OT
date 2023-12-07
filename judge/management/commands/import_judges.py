import csv
import os
from django.conf import settings
from django.core.management.base import BaseCommand
from judge.models import Judge
from django.core.files import File
from django.core.files.images import ImageFile
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Importa datos desde un archivo CSV a la base de datos de Django'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Ruta del archivo CSV a importar')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']

        # Resetear los objetos de la base de datos
        self.reset_database_objects()

        with open(csv_file_path, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row

            for row in csv_reader:
                first_name, last_name, job = row

                # Reemplazar "-" con espacio en subject
                job = job.replace('-', ' ')
                job = job.replace('_', ',')

                # Crear instancia de Judge
                judge = Judge(
                    first_name=first_name,
                    last_name=last_name,
                    job=job,
                )
                judge.save()

                # Verificar si hay apellidos antes de construir el nombre del archivo de la imagen
                if last_name:
                    avatar_filename = f"{first_name.lower()}_{last_name.lower()}.jpg"
                else:
                    avatar_filename = f"{first_name.lower()}.jpg"


                # Manejo de la imagen
                judge.avatar.name = f'judge/{avatar_filename}'
                judge.save()

        self.stdout.write(self.style.SUCCESS('Importación de jueces CSV completada.'))

    def reset_database_objects(self):
        Judge.objects.all().delete()
