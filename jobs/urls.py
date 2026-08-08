from django.urls import path
from . import views

urlpatterns = [

    # Website URLs
    path("", views.JobListView.as_view(), name="job_list"),

    path("<int:job_id>/", views.JobDetailView.as_view(), name="job_detail"),

    path("company/<str:company_name>/", views.company_jobs, name="company_jobs"),

    path("create/", views.JobCreateView.as_view(), name="create_job"),

    path("<int:job_id>/update/", views.JobUpdateView.as_view(), name="update_job"),

    path("<int:job_id>/delete/", views.JobDeleteView.as_view(), name="delete_job"),

    # API URLs
    path(
        "api/jobs/",
        views.JobListAPIView.as_view(),
        name="job_list_api",
    ),

    path(
        "api/jobs/<int:job_id>/",
        views.JobDetailAPIView.as_view(),
        name="job_detail_api",
    ),
]