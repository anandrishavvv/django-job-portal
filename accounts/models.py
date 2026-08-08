from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
import os


def validate_resume(value):

    ext = os.path.splitext(value.name)[1].lower()

    allowed_extensions = [
        ".pdf",
        ".doc",
        ".docx",
    ]

    if ext not in allowed_extensions:
        raise ValidationError(
            "Only PDF, DOC and DOCX files are allowed."
        )

    max_size = 2 * 1024 * 1024

    if value.size > max_size:
        raise ValidationError(
            "Resume size should not exceed 2 MB."
        )


class CandidateProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    resume = models.FileField(
        upload_to="resumes/",
        validators=[
            validate_resume,
        ],
    )

    phone = models.CharField(
        max_length=15,
    )

    def __str__(self):
        return self.user.username