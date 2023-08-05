from django.db import models
from django.contrib.auth.models import User
from journeys.models import Journey


class Like(models.Model):
    """
    Like model, related to User and Journey.
    'owner' is a User instance and 'journey' is a Journey instance.
    'unique_together' makes sure a user can't like the same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    journey = models.ForeignKey(
        Journey, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'journey']
    
    def __str__(self):
        return f'{self.owner} {self.journey}'

