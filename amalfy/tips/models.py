from django.db import models


class Tip(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True
    )
    content = models.TextField()
    order = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return str(self.name)
