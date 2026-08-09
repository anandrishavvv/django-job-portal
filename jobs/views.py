from rest_framework import viewsets

from .models import Job
from .serializers import JobSerializer


class JobViewSet(viewsets.ModelViewSet):

    queryset = Job.objects.select_related(
        "company"
    ).all()

    serializer_class = JobSerializer