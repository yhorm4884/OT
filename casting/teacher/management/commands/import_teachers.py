import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from competitor.models import Competitor, MusicStyle

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
    #             first_name, last_name, birthdate, city, job, hobbies, music_styles_str = row

    #             # Corregir el formato de la fecha
    #             birthdate = datetime.strptime(birthdate, '%d/%m/%Y').strftime('%Y-%m-%d')

    #             # Reemplazar "_" con espacio en job y hobbies
    #             job = job.replace('-', ' ')
    #             hobbies = hobbies.replace('_', ',')
    #             hobbies = hobbies.replace('-', ' ')
    #             # Reemplazar "-" con espacio en city
    #             city = city.replace('-', ' ')

    #             competitor = Competitor(
    #                 first_name=first_name,
    #                 last_name=last_name,
    #                 birthdate=birthdate,
    #                 city=city,
    #                 job=job,
    #                 hobbies=hobbies,
    #             )
    #             competitor.save()

    #             music_styles_list = music_styles_str.split('_')
    #             for style_name in music_styles_list:
    #                 style, created = MusicStyle.objects.get_or_create(name=style_name.strip())
    #                 competitor.music_styles.add(style)

    #     self.stdout.write(self.style.SUCCESS('Importación desde CSV completada.'))

    # def reset_database_objects(self):
    #     Competitor.objects.all().delete()
    #     MusicStyle.objects.all().delete()
