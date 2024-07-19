# django commands to wait for the db to be available.

from typing import Any
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any):
        pass
