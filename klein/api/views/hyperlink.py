from rest_framework import viewsets
from api import models, serializers


class HyperlinkViewSet(viewsets.ModelViewSet):
    queryset = models.Hyperlink.objects.all()
    serializer_class = serializers.HyperlinkSerializer
