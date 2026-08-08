from django.shortcuts import (
    render,
    
)

from django.core.paginator import Paginator
from django.db.models import Q

from .models import Job, Company
from .forms import JobForm
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import RecruiterRequiredMixin






@login_required
def company_jobs(request, company_name):

    jobs = Job.objects.filter(
        company=company_name
    )

    context = {
        "jobs": jobs,
        "company_name": company_name,
    }

    return render(
        request,
        "jobs/company_jobs.html",
        context
    )


class JobListView(LoginRequiredMixin, ListView):

    model = Job

    template_name = "jobs/job_list.html"

    context_object_name = "jobs"

    paginate_by = 5

    def get_queryset(self):

        queryset = Job.objects.select_related(
            "company"
        ).all()

        search = self.request.GET.get("search")
        company = self.request.GET.get("company")
        location = self.request.GET.get("location")
        remote = self.request.GET.get("remote")
        sort = self.request.GET.get("sort")

        # Search
        if search:

            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(company__name__icontains=search) |
                Q(location__icontains=search)
            )

        # Company Filter
        if company:

            queryset = queryset.filter(
                company__name=company
            )

        # Location Filter
        if location:

            queryset = queryset.filter(
                location=location
            )

        # Remote Filter
        if remote:

            queryset = queryset.filter(
                remote=True
            )

        # Sorting
        if sort == "title":

            queryset = queryset.order_by("title")

        elif sort == "-title":

            queryset = queryset.order_by("-title")

        elif sort == "company":

            queryset = queryset.order_by("company__name")

        elif sort == "-company":

            queryset = queryset.order_by("-company__name")

        elif sort == "newest":

            queryset = queryset.order_by("-id")

        elif sort == "oldest":

            queryset = queryset.order_by("id")

        else:

            queryset = queryset.order_by("-id")

        return queryset

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["companies"] = Company.objects.all()

        context["locations"] = Job.objects.values_list(
            "location",
            flat=True
        ).distinct()

        return context
class JobDetailView(LoginRequiredMixin, DetailView):

    model = Job

    template_name = "jobs/job_detail.html"

    context_object_name = "job"

    pk_url_kwarg = "job_id"




class JobCreateView(LoginRequiredMixin,RecruiterRequiredMixin,CreateView):

    model = Job

    form_class = JobForm

    template_name = "jobs/create_job.html"

    success_url = reverse_lazy("job_list")


class JobUpdateView(LoginRequiredMixin,RecruiterRequiredMixin,UpdateView):

    model = Job

    form_class = JobForm

    template_name = "jobs/update_job.html"

    pk_url_kwarg = "job_id"

    success_url = reverse_lazy("job_list")

class JobDeleteView(LoginRequiredMixin,RecruiterRequiredMixin,DeleteView):

    model = Job

    template_name = "jobs/delete_job.html"

    pk_url_kwarg = "job_id"

    success_url = reverse_lazy("job_list")