from django.db import models
from .behaviours import Authorable, Permalinkable, Timestampable, Publishable, BlogPostManager


class BlogPost(Authorable, Permalinkable, Timestampable, Publishable, models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    url_name = "blog-post"
    objects = BlogPostManager()
    
    @property
    def slug_source(self):
        return self.title
