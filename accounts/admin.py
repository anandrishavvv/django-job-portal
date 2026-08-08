from django.contrib import admin

from .models import CandidateProfile


@admin.register(CandidateProfile)
class CandidateProfileAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "phone",
    )

    search_fields = (
        "user__username",
        "phone",
    )