from django.core.exceptions import PermissionDenied
from application.models.dto.user_model import *


def authorization(*permissions):
    """
    Authorization decorator.
    :param level: UserLevel
    """
    def decorator(f):
        def wraps(request, *args, **kwargs):
            if not request.user:
                raise PermissionDenied

            # request.user is root
            if request.user.permission == UserPermission.root:
                return f(request, *args, **kwargs)

            if request.user.permission in permissions:
                return f(request, *args, **kwargs)
            else:
                raise PermissionDenied
        return wraps
    return decorator
