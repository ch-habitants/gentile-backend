from gentile.models.canton import Canton
from django.db import models


class Commune(models.Model):

    name_fr = models.CharField(max_length=50)
    canton = models.ForeignKey(Canton, on_delete=models.CASCADE)

    gentile_fr = models.CharField(max_length=100)

    searchable_name = models.CharField(max_length=100)
    searchable_gentile = models.CharField(max_length=150)
