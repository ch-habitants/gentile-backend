from gentile.models import Canton, Commune
from rest_framework import serializers


class CantonSerializer(serializers.ModelSerializer[Canton]):
    class Meta:
        model = Canton
        fields = ['name_fr', 'iso']


class CommuneSerializer(serializers.ModelSerializer[Commune]):
    class Meta:
        model = Commune
        fields = ['name_fr', 'canton', 'gentile_fr']
        depth = 1
