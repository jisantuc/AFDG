from __future__ import unicode_literals

from django.db import models

import uuid


class AFDGUser(models.Model):
    """AFDG User model class tracking wins and total games

    There's no secret or password or anything like that because there's
    no need to verify that people are who they say they are for this
    application. If a user claims to be hungriestHippo943, the app
    believes them.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=31, null=False, unique=True)
    wins = models.IntegerField(default=0, null=False)
    games = models.IntegerField(default=0, null=False)
