from django.db import models
from django.contrib.auth.models import User


class Journey(models.Model):
    """
    Journey model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
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