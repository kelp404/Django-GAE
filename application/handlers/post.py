from django.http import HttpResponse
from application.decorators.auth import *


@authorization(UserPermission.normal, UserPermission.root)
def create_post(request):
    import logging
    logging.error(request.body)
    return HttpResponse(status=200)
