from rest_framework import viewsets
from api import models, serializers


class HyperlinkAliasViewSet(viewsets.ModelViewSet):
    queryset = models.HyperlinkAlias.objects.all()
    serializer_class = serializers.HyperlinkAliasSerializer
