from rest_framework import viewsets
from rest_framework.response import Response
from api import models, serializers


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
