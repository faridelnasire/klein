from django.db import models


class HyperlinkAlias(models.Model):
    hyperlink = models.ForeignKey(
        'Hyperlink',
        on_delete=models.PROTECT
    )
    alias = models.CharField(max_length=2048, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
