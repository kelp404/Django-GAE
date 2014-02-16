from django.template import loader, RequestContext, Context
from django.http import HttpResponseNotFound, HttpResponseServerError


def page_not_found(request):
    template = loader.get_template('error/default.html')
    model = {
        'status': 404,
        'exception': '%s Not Found' % request.path,
    }
    return HttpResponseNotFound(template.render(RequestContext(request, model)))

def server_error(request):
    template = loader.get_template('error/default.html')
    model = {
        'status': 500,
        'exception': ''
    }
    return HttpResponseServerError(template.render(Context(model)))
