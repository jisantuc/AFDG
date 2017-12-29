from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class UserWinTracker(models.Model):
    """AFDG User model class tracking wins and total games

    There's no secret or password or anything like that because there's
    no need to verify that people are who they say they are for this
    application. If a user claims to be hungriestHippo943, the app
    believes them.
    """

    user = models.ForeignKey(User, null=False)
    wins = models.IntegerField(default=0, null=False)
    games = models.IntegerField(default=0, null=False)
