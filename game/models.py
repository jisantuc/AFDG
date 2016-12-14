import uuid

from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.gis.db import models as gis_models
from django.contrib.auth.models import User


class AFDGGame(models.Model):
    """Model object tracking information about participants in
    and winners of games"""

    id = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4)
    players = models.ManyToManyField(User)
    winner = models.ForeignKey(User, null=True,
                               related_name='%(class)s_winner')

    @classmethod
    def for_user(self, user):
        """Saved query to return only games with a specific user
        """

        return self.objects.filter(players=user)


class AFDGTile(models.Model):
    """Model object tracking tiles and their states in games"""

    id = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4)
    game = models.ForeignKey(AFDGGame, null=False)
    walls = ArrayField(
        models.CharField(max_length=5,
                         choices=[('north', 'north'),
                                  ('south', 'south'),
                                  ('east', 'east'),
                                  ('west', 'west')]),
        size=4
    )
    owner = models.ForeignKey(User, null=False)
    is_base = models.BooleanField(null=False, default=False)
    location = gis_models.PointField(null=False)

    def visible_from(self):
        return AFDGTile.objects.filter(
            game=self.game, location__distance_lt=1
        )
