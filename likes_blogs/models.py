from django.db import models
from django.contrib.auth.models import User
from blogs.models import Blog


class LikeBlog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(
        Blog, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'blog']

    def __str__(self):
        return f'{self.owner} {self.blog}'
