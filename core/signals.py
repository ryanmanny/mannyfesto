from django.db.models.signals import pre_save

from core import models


def post_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = instance._get_unique_slug()
    instance.preview = instance._get_preview()  # Always recalculate preview


pre_save.connect(post_pre_save, sender=models.Post)
pre_save.connect(post_pre_save, sender=models.HTMLPost)
