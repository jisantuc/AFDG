import uuid

from django.db import models

from userdata.models import AFDGUser


class AFDGGame(models.Model):
    """Model object tracking information about participants in
    and winners of games"""

    id = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4)
    players = models.ManyToManyField(AFDGUser)
    winner = models.ForeignKey(AFDGUser, null=True,
                               related_name='%(class)s_winner')

    @classmethod
    def for_user(self, user):
        """Saved query to return only games with a specific user
        """

        return self.objects.filter(players=user)
