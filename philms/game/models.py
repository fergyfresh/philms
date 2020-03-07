import string
import random

from django.db import models
from django.core.validators import MinLengthValidator


class Game(models.Model):
    name = models.CharField(db_index=True, max_length=4)
    is_open = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.name = "".join(random.choice(string.ascii_uppercase)
                                for i in range(4))
        super(Game, self).save(*args, **kwargs)


class Player(models.Model):
    name = models.CharField(max_length=16,
                            validators=[MinLengthValidator(4)])
    is_owner = models.BooleanField(default=False)
    game = models.ForeignKey(to=Game, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'game')
        constraints = [
            models.CheckConstraint(check=~models.Q(
                name=""), name="non_empty_name")
        ]
