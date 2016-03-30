from django.test import TestCase
from unittest.mock import Mock
from django.utils import timezone
from .models import BlogPost


class BlogPostTestCase(TestCase):

    def test_blog_post_is_published(self):
        blogpost = Mock(spec=BlogPost)
        blogpost.publish_date = timezone.now()
        self.assertTrue(blogpost.is_published)
