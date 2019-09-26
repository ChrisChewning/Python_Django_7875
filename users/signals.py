#django docs recommend here instead of models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_profile(sender, instance, **kwargs):
    instance.profile.save()


#post_save signal when a user is created
#User model is sending the signal
#receiver receives the signal
#Profile  

#when a user is saved, send the signal.
#The signal will be received by the createProfile fn.
#if user was created, create a Profile objects with 

#the signal is post_save.