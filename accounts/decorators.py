from functools import wraps
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from .models import User


def role_required(*roles):
    """Izinkan akses hanya untuk role tertentu."""
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('accounts:login')
            if not request.user.has_role(*roles):
                raise PermissionDenied
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator


def min_role_required(min_role):
    """Izinkan akses untuk role dengan level minimal tertentu."""
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('accounts:login')
            if not request.user.has_min_role(min_role):
                raise PermissionDenied
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator


# Shortcut decorators
scoring_required = role_required(User.SCORING, User.MANAGER, User.SUPERVISOR, User.ADMIN, User.SUPERADMIN)
manager_required = min_role_required(User.MANAGER)
supervisor_required = min_role_required(User.SUPERVISOR)
admin_required = min_role_required(User.ADMIN)
superadmin_required = role_required(User.SUPERADMIN)
