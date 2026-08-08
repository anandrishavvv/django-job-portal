from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import CandidateProfile


@receiver(post_save, sender=User)
def create_candidate_profile(sender, instance, created, **kwargs):

    if created:
        CandidateProfile.objects.create(user=instance)


@receiver(pre_save, sender=CandidateProfile)
def delete_old_resume(sender, instance, **kwargs):

    if not instance.pk:
        return

    try:
        old_profile = CandidateProfile.objects.get(pk=instance.pk)
    except CandidateProfile.DoesNotExist:
        return

    old_resume = old_profile.resume
    new_resume = instance.resume

    if (
        old_resume
        and old_resume != new_resume
    ):
        old_resume.delete(save=False)