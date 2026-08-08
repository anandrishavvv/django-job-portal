from django.contrib import admin

from .models import Company, Job


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "location",
    )


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "company",
        "location",
        "remote",
    )

    list_filter = (
        "company",
        "remote",
    )

    search_fields = (
        "title",
        "company__name",
        "location",
    )