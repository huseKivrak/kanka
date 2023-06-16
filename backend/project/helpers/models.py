from django.db import models


class TrackingModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text='Date/time created'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        help_text='Date/time updated'
    )

    class Meta:
        abstract = True
        ordering = ('-created_at',)

