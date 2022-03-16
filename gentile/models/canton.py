from django.db import models


class Canton(models.Model):

    name_fr = models.CharField(max_length=30)
    iso = models.CharField(max_length=2)
