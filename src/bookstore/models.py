from django.db import models


class Book(models.Model):
    external_id = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100, blank=True)
    acquired = models.BooleanField(default=False)
    published_year = models.IntegerField(blank=True)
    thumbnail = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.title
