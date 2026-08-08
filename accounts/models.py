from django.contrib.auth.models import User
from django.db import models


class CandidateProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    resume = models.FileField(
        upload_to="resumes/"
    )

    phone = models.CharField(
        max_length=15
    )

    def __str__(self):

        return self.user.username