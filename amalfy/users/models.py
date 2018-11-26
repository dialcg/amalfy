from django.db import models
from django.contrib.auth.models import AbstractUser
from tips.models import Tip


class User(AbstractUser):
    last_checked_tip = models.ForeignKey(
        Tip,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )


class DayMood(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    score = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}@{}'.format(
            self.user,
            self.date
        )

