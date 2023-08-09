from django.db import models
from django.contrib.auth.models import User
from stops.models import Stop


class CommentStop(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    