from django.core.exceptions import PermissionDenied


class RecruiterRequiredMixin:

    def dispatch(self, request, *args, **kwargs):

        if request.user.groups.filter(
            name="Recruiter"
        ).exists():

            return super().dispatch(
                request,
                *args,
                **kwargs
            )

        raise PermissionDenied
    