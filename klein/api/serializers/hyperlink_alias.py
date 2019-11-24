from django.http import HttpResponseBadRequest
from rest_framework import serializers
from api import models


class HyperlinkAliasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HyperlinkAlias
        fields = ['id', 'hyperlink', 'alias', 'created_on']

    def create(self, validated_data):
        if validated_data['alias'][0] == '_':
            raise serializers.ValidationError('Can not create an alias that starts with _')
        return models.HyperlinkAlias.objects.create(**validated_data)
