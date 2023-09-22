from django.db import models
from django.contrib.auth.models import User
from stops.models import Stop


class LikeStop(models.Model):
    """
    LikeStop model, related to User, Journey, and Stop.
    'owner' is a User instance, 'journey' is a Journey instance,
    and 'stop' is a stop instance.
    'unique_together' makes sure a user can't like the same stop twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    stop = models.ForeignKey(
        Stop, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'stop']

    def __str__(self):
        return f'{self.owner} {self.stop}'
