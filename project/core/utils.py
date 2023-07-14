from django.db import models


# Utility for adding created/updated timestamps
class TrackingModel(models.Model):
    '''Adds created_at and updated_at fields'''
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)
