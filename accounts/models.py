from django.db import models
from django.contrib import auth
from django.db.models.signals import post_save #for updating and saving user profiles
from django.dispatch import receiver

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username) 

class Profile(models.Model):
    MEDIUMS_CHOICES = (
        ('Print', 'Print'),
        ('Digital', 'Digital'),
        ('Radio', 'Radio'),
        ('Vlog', 'Vlog'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    career = models.CharField(max_length=250, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=250, blank=True)
    clients = models.TextField(blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.created(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
