import string
import random

from django.db import models


class Game(models.Model):
    code = models.CharField(db_index=True, max_length=4)
    is_open = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.code = "".join(
                random.choice(string.ascii_uppercase) for i in range(4)
            )
        super(Game, self).save(*args, **kwargs)
