from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(
    "api/jobs",
    views.JobViewSet,
    basename="job"
)

urlpatterns = [

    # Website URLs
    path("", views.JobListView.as_view(), name="job_list"),

    path("<int:job_id>/", views.JobDetailView.as_view(), name="job_detail"),

    path(
        "company/<str:company_name>/",
        views.company_jobs,
        name="company_jobs",
    ),

    path(
        "create/",
        views.JobCreateView.as_view(),
        name="create_job",
    ),

    path(
        "<int:job_id>/update/",
        views.JobUpdateView.as_view(),
        name="update_job",
    ),

    path(
        "<int:job_id>/delete/",
        views.JobDeleteView.as_view(),
        name="delete_job",
    ),
]

urlpatterns += router.urls