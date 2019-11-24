from django.db import models


class HyperlinkView(models.Model):
    hyperlink = models.ForeignKey(
        'Hyperlink',
        on_delete=models.PROTECT
    )
    hyperlink_alias = models.ForeignKey(
        'HyperlinkAlias',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    ip_address = models.GenericIPAddressField()
    viewed_on = models.DateTimeField(auto_now_add=True)
