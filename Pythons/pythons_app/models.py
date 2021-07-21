from django.db import models


class Python(models.Model):
    name = models.CharField(
        max_length=15,
    )
    description = models.TextField()
    image = models.URLField()
