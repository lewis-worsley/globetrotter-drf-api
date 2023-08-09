from django.db import models


class News(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(
        upload_to='images/', default='../default-journey-image_b1f0wk.jpg', 
        blank=True
    )

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.id} {self.title}'
