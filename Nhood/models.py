from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    occupants = models.IntegerField(null=True)
    admin = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(cls):
        return cls.name

    @classmethod
    def get_nhoods(cls):
        return cls.objects.all()

    @classmethod
    def join_nhood(cls,n_id):
        nhood = Neighbourhood.objects.get(pk=n_id)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Profile")
    hood = models.ForeignKey(Neighbourhood, null=True)
    email = models.EmailField(max_length=254)

    def __str__(cls):
        return cls.user
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

    def __str__(cls):
        return cls.name
