from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.shortcuts import redirect

def admin_required(function=None, redirect_url='cafe:staff_dashboard'):
    """
    Decorator for views that checks that the user is logged in and is an admin,
    redirecting to the staff dashboard with an error message if necessary.
    """
    def check_role(user):
        if not user.is_authenticated:
            return False
        if user.role == 'admin' or user.is_superuser:
            return True
        return False

    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if check_role(request.user):
                return view_func(request, *args, **kwargs)
            else:
                messages.error(request, "Unauthorized Access! You do not have permission to view this page.")
                return redirect(redirect_url)
        return _wrapped_view

    if function:
        return decorator(function)
    return decorator

def staff_required(function=None, redirect_url='cafe:login'):
    """
    Decorator for views that checks that the user is logged in and is a staff member or admin.
    """
    def check_role(user):
        if not user.is_authenticated:
            return False
        if user.role in ['admin', 'staff'] or user.is_superuser:
            return True
        return False

    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if check_role(request.user):
                return view_func(request, *args, **kwargs)
            else:
                messages.error(request, "Unauthorized Access! Please log in as a staff member.")
                return redirect(redirect_url)
        return _wrapped_view

    if function:
        return decorator(function)
    return decorator
