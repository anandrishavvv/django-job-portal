from functools import wraps

from django.core.exceptions import PermissionDenied


def recruiter_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if request.user.groups.filter(
            name="Recruiter"
        ).exists():

            return view_func(
                request,
                *args,
                **kwargs
            )

        raise PermissionDenied

    return wrapper