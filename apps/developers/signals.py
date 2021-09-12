import logging
import os
from django.contrib.auth.models import User
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
from .models import Profile

logger = logging.getLogger(__name__)


@receiver(post_delete, sender=Profile, dispatch_uid="delete_img_profile")
def delete_img_profile(sender, instance, **kwargs):
    if not instance.image:
        return
    os.remove(instance.image.path)
    logger.info(f"image <{instance.image}> of <{instance}> for {sender} was deleted")


@receiver(post_save, sender=Profile, dispatch_uid="profile_updated_created")
def profile_updated_created(sender, instance, created, **kwargs):
    # created: if you saving obj after creating new obj ==> create = True
    # created: if you saving obj after updating obj already exist ==> create = False
    if created:
        print("CREATED")
    else:
        print("UPDATED")


@receiver(post_save, sender=User, dispatch_uid="create_profile")
def create_profile(sender, instance, created, **kwargs):
    updated = not created
    if updated:
        return

    profile = Profile(user=instance)
    profile.save()
    logger.info(f"profile <{profile}> with user <{instance}> has been created")


@receiver(post_delete, sender=Profile, dispatch_uid="delete_profile")
def delete_profile(sender, instance, **kwargs):
    User.objects.filter(username__iexact=instance.user.username).delete()
    logger.info(f"profile <{instance}> with user <{instance.user}> has been delete")