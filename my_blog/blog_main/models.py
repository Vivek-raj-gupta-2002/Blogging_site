from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class post(models.Model):
    Heading = models.CharField(max_length=200, unique=True)
    Content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    Author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    Created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-Created_on']

    def __str__(self):
        return self.Heading