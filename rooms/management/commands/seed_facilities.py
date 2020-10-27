from django.core.management.base import BaseCommand
from rooms.models import Facilities


class Command(BaseCommand):
    help = "This commend creates amenites"

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for a in facilities:
            Facilities.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} - Facilities created"))
