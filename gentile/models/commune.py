from gentile.models.canton import Canton
from django.db import models

from typing import Any
from unidecode import unidecode


class Commune(models.Model):

    name_fr = models.CharField(max_length=50)
    canton = models.ForeignKey(Canton, on_delete=models.CASCADE)

    gentile_fr = models.CharField(max_length=100)

    searchable_name = models.CharField(max_length=100, blank=True)
    searchable_gentile = models.CharField(max_length=150)

    def save(self, *args: Any, **kwargs: Any) -> None:
        def generate_searchable_string(base_string: str) -> str:
            return (
                unidecode(base_string)
                .replace('-', ' ')
                .replace(',', '')
                .replace('Saint', 'saint st')
                .lower()
            )

        self.searchable_name = generate_searchable_string(self.name_fr)
        self.searchable_gentile = generate_searchable_string(self.gentile_fr)

        super().save(*args, **kwargs)
