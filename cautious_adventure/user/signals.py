from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import Profile


def create_profile(sender, instance, created, **kwargs):
    """When creating user, the profile will be created"""
    if created:
        prof_name = ""
        if instance.first_name:
            prof_name += instance.first_name
        if instance.last_name:
            prof_name += " " + instance.last_name

        Profile.objects.create(
            prof_user = instance,
            prof_name = prof_name.strip(),
            prof_username = instance.username,
            prof_email = instance.email
        )


def delete_user(sender, instance, **kwargs):
    """When profile is deleted, the user will be deleted"""
    try:
        user = instance.prof_user
        user.delete()
    except:
        pass


post_save.connect(create_profile, sender=User)
post_delete.connect(delete_user, sender=Profile)