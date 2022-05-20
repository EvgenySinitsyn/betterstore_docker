from django.db import models


class KeysValues(models.Model):

    KEY = models.CharField(max_length=255, unique=True)
    VALUE = models.JSONField()
    unix_time = models.PositiveBigIntegerField()

    def __str__(self):
        return self.KEY

