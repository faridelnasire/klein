from django.http import Http404, HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from api import models, serializers
from api.utils import decode_hyperlink_id


class HyperlinkViewSet(viewsets.ModelViewSet):
    queryset = models.Hyperlink.objects.all()
    serializer_class = serializers.HyperlinkSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=201, data=serializer.data)
        else:
            return Response(status=400)


class HyperlinkRedirectView(APIView):
    def get(self, request, slug, format=None):
        # Ignore any static file requests that make it to this point
        if '.' in slug:
            raise Http404('Short URL does not exist')

        # See if an alias exists
        hyperlink_aliases = models.HyperlinkAlias.objects.filter(
            alias=slug
        )
        if hyperlink_aliases.exists():
            return HttpResponseRedirect(hyperlink_aliases.first().hyperlink.url)

        # See if it's a Hyperlink with a slug that was taken by an alias
        if slug[0] == '_':
            slug = slug[1:]

        # See if Hyperlink exists
        hyperlinks = models.Hyperlink.objects.filter(
            id=decode_hyperlink_id(slug)
        )
        if hyperlinks.exists():
            return HttpResponseRedirect(hyperlinks.first().url)
        else:
            raise Http404('Short URL does not exist')
