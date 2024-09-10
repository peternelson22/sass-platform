from typing import Any
from django.core.management.base import BaseCommand, CommandParser

from subscriptions import utils as sub_utils

class Command(BaseCommand):
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--clear-dangling', action='store_true', default=False)
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        clear_dangling = options.get('clear_dangling')
        if clear_dangling:
            print('Clearing dangling subs')
            sub_utils.clear_dangling_subs()
        else:
            print('Sync active subs')