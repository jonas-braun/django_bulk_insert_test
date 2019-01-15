import random
from django.core.management import BaseCommand

from inserter.models import Item


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        items = []
        for i in range(5):
            item = Item(attribute=random.randint(0, 1000000))
            items.append(item)

        print(items)

        Item.objects.bulk_create(items)

        print(Item.objects.filter(attribute__in=[item.attribute for item in items]))

