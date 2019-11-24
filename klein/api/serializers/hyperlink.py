from django.conf import settings
from rest_framework import serializers
from api import models
from api.utils import encode_hyperlink_id


class HyperlinkSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()

    class Meta:
        model = models.Hyperlink
        fields = ['id', 'url', 'short_url', 'created_on']

    def get_short_url(self, instance):
        slug = encode_hyperlink_id(instance.id)

        # Figure out if we have to prepend the slug with a _
        if models.HyperlinkAlias.objects.filter(alias=slug).exists():
            slug = '_%s' % (slug)

        return '%s/%s' % (
            settings.BASE_URL,
            slug,
        )

    def create(self, validated_data):
        existing_hyperlinks = models.Hyperlink.objects.filter(
            url__iexact=validated_data['url']
        )
        if existing_hyperlinks.exists():
            return existing_hyperlinks.first()

        return models.Hyperlink.objects.create(**validated_data)
