from application.decorators.auth_decorator import *
from django.template.response import TemplateResponse


def home_view(request):
    response = TemplateResponse(request, 'base.html', {'x': 'GAE'})
    return response
