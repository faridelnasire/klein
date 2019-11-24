from rest_framework import serializers
from api import models


class HyperlinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hyperlink
        fields = ['id', 'url']
