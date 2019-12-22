""" For every new user, it must be create a profile with default.jpg image.
    Django documentation recommands to create a seperate file for this, 
    insted of including models.py to avoid side effects of import. 
"""
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:

        # Creates a profile object with instance of user.
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):

    # Saves profile object which is created above.
    instance.profile.save()