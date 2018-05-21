from django.db import models
from django.contrib import auth
from django.db.models.signals import post_save #for updating and saving user profiles
from django.dispatch import receiver


# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username) 

class UserProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE),
    MEDIUMS_CHOICES = (
        ('Print', 'Print'),
        ('Digital', 'Digital'),
        ('Radio', 'Radio'),
        ('Vlog', 'Vlog'),
    )
    career = models.CharField(max_length=250, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=250, blank=True)
    clients = models.TextField(blank=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

# Save, and Create
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfileModel.objects.created(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
