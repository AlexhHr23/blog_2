from django.db import models
import datetime

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()
    date = models.DateField(default=datetime.date.today)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/images')

    def __str__(self):
        return f"Image for {self.post.title}"
