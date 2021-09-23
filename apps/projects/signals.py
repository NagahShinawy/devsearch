import logging
import os

from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from .models import Project

logger = logging.getLogger(__name__)


def get_project_representation(instance):
    project = f"{instance.uuid}-{instance.title}" if instance.uuid else instance.title
    return project


@receiver(pre_save, sender=Project, dispatch_uid="update_slug")
def update_slug(sender, instance, **kwargs):
    project = get_project_representation(instance)
    if instance.slug is not None:
        return
    instance.slug = slugify(instance.title)
    logger.info(f"Update 'slug' for {sender} <{project}> to <{instance.slug}>")


@receiver(post_delete, sender=Project, dispatch_uid="delete_img_project")
def delete_img_project(sender, instance, **kwargs):
    if not instance.image:
        return
    os.remove(instance.image.path)
    logger.info(f"image <{instance.image}> of <{instance}> for {sender} was deleted")