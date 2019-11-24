from rest_framework import serializers
from api import models
from api.utils import encode_hyperlink_id


class HyperlinkSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()

    class Meta:
        model = models.Hyperlink
        fields = ['id', 'url', 'short_url', 'created_on']

    def get_short_url(self, instance):
        return encode_hyperlink_id(instance.id)
