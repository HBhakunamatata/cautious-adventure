from django.db import models
from uuid import uuid4
from user.models import Profile

# Create your models here.


class Category(models.Model):
    """category for topics"""
    cat_id = models.UUIDField(primary_key=True, unique=True, editable=True, default=uuid4)
    cat_name = models.CharField(max_length=100, null=False, blank=False)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cat_name


class Topic(models.Model):
    """topic model"""
    topic_id = models.UUIDField(primary_key=True, unique=True, editable=True, default=uuid4)
    topic_by = models.ForeignKey(Profile, null=False, on_delete=models.CASCADE)
    topic_cat = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)
    topic_subject = models.CharField(max_length=500, null=False, blank=False)
    view_count = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic_subject


class Post(models.Model):
    """post model"""
    post_id = models.UUIDField(primary_key=True, unique=True, editable=True, default=uuid4)
    post_by = models.ForeignKey(Profile, null=False, on_delete=models.CASCADE)
    post_topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=False)
    post_content = models.TextField(null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_content