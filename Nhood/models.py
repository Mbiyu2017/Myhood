from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    occupants = models.IntegerField()
    admin = models.CharField(max_length=30)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighbourhood, null=True)
    email = models.EmailField(max_length=254)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Business(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(Profile)
    neighbourhood = models.ForeignKey(Neighbourhood)
    email = models.EmailField(max_length=254)
