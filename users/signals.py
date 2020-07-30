from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

from users.models import Profile



@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created,*args, **kwargs):
    if created:
		# Send creation email
		# verify email address
        Profile.objects.create(user=instance)
		print("userCreated")
	else:
		instance.profile.save()
		print("account saved")
