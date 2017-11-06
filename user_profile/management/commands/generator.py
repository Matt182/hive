from django.core.management import BaseCommand
from faker import Faker

from user_profile.models import Profile


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--delete',
            action='store_true',
            default=False,
            help='Delete users',
        )

        parser.add_argument(
            '--generate',
            action='store_true',
            default=False,
            help='Generates users',
        )

    def handle(self, *args, **options):
        if options['delete']:
            clear()
        if options['generate']:
            generate()


def generate():
    faker = Faker()
    for i in range(5):
        Profile.objects.create(id=i, name=faker.name(), email=faker.email(), password=faker.first_name())


def clear():
    Profile.objects.all().delete()
