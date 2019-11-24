from django.db import models


class Hyperlink(models.Model):
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    url = models.URLField(max_length=2048)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (
            self.id,
            self.url
        )
