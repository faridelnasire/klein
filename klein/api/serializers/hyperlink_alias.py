from django.http import HttpResponseBadRequest
from rest_framework import serializers
from api import models
from api.utils import decode_hyperlink_id


class HyperlinkAliasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HyperlinkAlias
        fields = ['id', 'hyperlink', 'alias', 'created_on']

    def create(self, validated_data):
        # Protect _ prefix
        if validated_data['alias'][0] == '_':
            raise serializers.ValidationError('Can not create an alias that starts with _')

        # Make sure no Hyperlink with this slug already exists
        if models.Hyperlink.objects.filter(
            id=decode_hyperlink_id(validated_data['alias'])
        ).exists():
            raise serializers.ValidationError('A hyperlink with this alias already exists')

        return models.HyperlinkAlias.objects.create(**validated_data)
