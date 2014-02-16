from django.shortcuts import render_to_response
from django.http import HttpResponseNotFound


def page_not_found(request):
    model = {
        'status': 404,
        'exception': 'Page Not Found',
    }
    return HttpResponseNotFound(render_to_response('error/default.html', model))
