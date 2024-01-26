from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

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