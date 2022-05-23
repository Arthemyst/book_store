from email.policy import default

from django.db import models


class Book(models.Model):
    external_id = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100)
    authors = models.JSONField(default=list)
    acquired = models.BooleanField(default=False)
    published_year = models.CharField(max_length=100, null=True, blank=True)
    thumbnail = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.title
