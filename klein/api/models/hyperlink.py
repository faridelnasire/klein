from django.db import models


class Hyperlink(models.Model):
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    url = models.CharField(max_length=2048)
