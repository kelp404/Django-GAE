from django.template.response import TemplateResponse


def home_view(request):
    response = TemplateResponse(request, 'home.html', {'x': 'GAE'})
    return response
