from django.db import models

class Book(models.Model):
    external_id = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    authors = models.JSONField()
    acquired = models.BooleanField()
    published_year = models.IntegerField()
    thumbnail = models.CharField(max_length=300)

    def __str__(self):
        return self.title
