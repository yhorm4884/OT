import csv
from django.core.management.base import BaseCommand
from teacher.models import Teacher

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
                first_name, last_name,subject = row

                # Reemplazar "-" con espacio en subject
                subject= subject.replace('-',' ')
                teacher = Teacher(
                    first_name= first_name,
                    last_name=last_name,
                    subject=subject,
                )
                teacher.save()
    
        self.stdout.write(self.style.SUCCESS('Importación desde CSV completada.'))

    def reset_database_objects(self):
        Teacher.objects.all().delete()
