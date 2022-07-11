from django.utils import timezone
from django.db import models

class Hit(models.Model):

    PAGEVIEW = 'PV'
    DOWNLOAD = 'DL'
    ACTIONS = (
        (PAGEVIEW, 'Article web page view'),
        (DOWNLOAD, 'Article download'),
    )

    publication = models.ForeignKey('Publication', on_delete=models.CASCADE)
    # ip_address = models.GenericIPAddressField()
    # user_agent = models.ForeignKey('UserAgent', on_delete=models.SET_NULL,
    #                                null=True, blank=True)
    action = models.CharField(max_length=2, choices=ACTIONS)

class Publication(models.Model):

    title = models.CharField(max_length=200)
    journal = models.ForeignKey('Journal', on_delete=models.CASCADE)
    # ... remaining fields omitted

class Journal(models.Model):

    title = models.CharField(max_length=255)
