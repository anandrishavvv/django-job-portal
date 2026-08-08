from django.urls import path
from . import views
urlpatterns = [
    path("",views.JobListView.as_view(),name="job_list",),
    path("create/", views.JobCreateView.as_view(), name="create_job"),
    path("<int:job_id>/edit/", views.JobUpdateView.as_view(), name="update_job"),
    path("<int:job_id>/delete/", views.JobDeleteView.as_view(), name="delete_job"),
    path("<int:job_id>/", views.JobDetailView.as_view(), name="job_detail"),
]