from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default='default-slug')
    raw_image = models.ImageField(default='default.png', blank=True)
    processed_image = models.ImageField(blank=True)
    author = models.ForeignKey(User, default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.name