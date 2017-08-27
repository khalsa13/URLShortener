from django.core.management.base import BaseCommand,CommandError
from shortener.models import deepURL

class Command(BaseCommand):
    help = 'Refreshes All Shortcode'

    def handle(self, *args, **options):
        return deepURL.objects.refresh_allcode()