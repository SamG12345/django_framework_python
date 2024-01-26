from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

# User Profile
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    companian = models.ManyToManyField("self", related_name="companianed_by", symmetrical=False, blank=True)
    date_created = models.DateTimeField("self", auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username

# Profile creation
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user = instance)
        user_profile.save()
post_save.connect(create_profile, sender=User)

# Written byt profile
class Lekh(models.Model):
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    body = models.CharField(max_length=200)
    date_created = models.DateTimeField(Profile, auto_now_add=True)
    likes = models.ManyToManyField(Profile, related_name="liked_by", symmetrical=False, blank=True)

    def no_of_likes(self):
        return self.likes.count()
    def __str__(self) -> str:
        return self.body