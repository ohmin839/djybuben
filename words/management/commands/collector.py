import io, urllib.request
from django.core.management.base import BaseCommand
from django.db import transaction

import pybuben
from pybuben.api import to_hayeren_word_set

from ...models import SampledWord

class Command(BaseCommand):
    def handle(self, *args, **options):
        before_count = SampledWord.objects.count()

        try:
            url = "https://news.am/arm/"
            req = urllib.request.Request(url)
            req.add_header("User-Agent", f"pybuben/{pybuben.__version__}")
            with urllib.request.urlopen(req) as res:
                reader = io.TextIOWrapper(res, encoding="utf-8")
                word_set = to_hayeren_word_set(reader)
                with transaction.atomic():
                    for word in word_set:
                        SampledWord.objects.update_or_create(text=word)
        except Exception as e:
            print(e)

        after_count = SampledWord.objects.count()
        print(f"{after_count - before_count} words added")
