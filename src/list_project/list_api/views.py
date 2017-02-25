from rest_framework import viewsets

from . import models, serializers


class ListItemViewSet(viewsets.ModelViewSet):
    """
    Create, read, update and delete list items in our database.
    """

    serializer_class = ListItemSerializer
    queryset = models.ListItem.objects.all()
