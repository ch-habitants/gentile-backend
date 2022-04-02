from rest_framework import mixins, viewsets

from gentile.models import Commune
from gentile.serializers import CommuneSerializer


class CustomViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    """
    Custom viewset allowing only for models to be listed and retrieved.
    """
    ...


class CommuneViewSet(CustomViewSet):
    """
    API endpoint to get all the communes and their gentilés.
    """
    queryset = Commune.objects.all().order_by('name_fr')
    serializer_class = CommuneSerializer
