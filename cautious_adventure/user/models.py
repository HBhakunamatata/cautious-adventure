from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    """User one-to-one field"""
    prof_id = models.UUIDField(primary_key=True, unique=True, editable=True, default=uuid4)
    prof_user = models.OneToOneField(User, null=False, blank=False, unique=True, on_delete=models.CASCADE)
    prof_username = models.CharField(max_length=200, null=False, blank=False)
    prof_name = models.CharField(max_length=200, null=True, blank=True)
    prof_email = models.CharField(max_length=100, null=True, blank=True)
    prof_photo = models.ImageField(blank=True, null=True, default='default-photo.jpg', upload_to='profiles')
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # result = self.prof_username
        # if self.prof_name:
        #     result = self.prof_name
        # return result
        return self.prof_username