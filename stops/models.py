from django.db import models
from django.contrib.auth.models import User
from journeys.models import Journey


class Stop(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    journey = models.ForeignKey(
        Journey, related_name='stops', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    countries = models.CharField(max_length=50)
    locations = models.CharField(max_length=400)
    image = models.ImageField(
        upload_to='images/', default='../default-journey-image_b1f0wk.jpg', 
        blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'