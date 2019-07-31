from django.db.models.signals import m2m_changed, post_save, pre_save
from django.dispatch import receiver

from cloud_provider.models import Region


@receiver(post_save, sender=Region)
def on_cluster_save(sender, instance=None, created=True, **kwargs):
    if created:
        instance.on_region_create()
