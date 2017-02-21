from rest_framework import serializers, viewsets

from . import models


class ListItemSerializer(serializers.ModelSerializer):
    """
    Serializer for converting JSON strings to a database object and
    for converting a database object to JSON string.
    """

    class Meta:
        model = models.ListItem
        fields = ('id', 'name', 'date_created',)
        read_only_fields = ('id', 'date_created',)


class ListItemViewSet(viewsets.ModelViewSet):
    """
    Viewset for managing list items via HTTP requests.
    """

    serializer_class = ListItemSerializer
    queryset = ListItem.objects.all()
