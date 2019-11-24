from django.http import Http404, HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from api import models, serializers
from api.utils import decode_hyperlink_id


class HyperlinkAliasViewSet(viewsets.ModelViewSet):
    queryset = models.HyperlinkAlias.objects.all()
    serializer_class = serializers.HyperlinkAliasSerializer
