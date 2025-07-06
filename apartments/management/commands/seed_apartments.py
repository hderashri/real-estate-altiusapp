from django.core.management.base import BaseCommand
from apartments.models import Apartment
from faker import Faker
import random

class Command(BaseCommand):
    help = "Seed database with fake apartment listings"

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(20):
            Apartment.objects.create(
                title=f"{fake.word().capitalize()} Apartment",
                location=fake.city(),
                price=random.randint(15000, 25000),
                bedrooms=random.choice([1, 2, 3])
            )
        self.stdout.write(self.style.SUCCESS("✅ Seeded 20 fake apartments"))