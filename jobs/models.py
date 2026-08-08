from django.db import models


class Company(models.Model):

    name = models.CharField(max_length=100)

    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Job(models.Model):

    title = models.CharField(max_length=200)

    company = models.ForeignKey(
    Company,
    on_delete=models.CASCADE,
    related_name="jobs"
)

    location = models.CharField(max_length=100)

    remote = models.BooleanField(default=False)

    def __str__(self):
        return self.title