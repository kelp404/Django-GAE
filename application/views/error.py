from django.template import loader, RequestContext, Context
from django import http


def page_not_found(request):
    template = loader.get_template('error/default.html')
    model = {
        'status': 404,
        'exception': '%s Not Found' % request.path,
    }
    return http.HttpResponseNotFound(template.render(RequestContext(request, model)))

def method_not_allowed(request):
    template = loader.get_template('error/default.html')
    model = {
        'status': 405,
        'exception': '%s Not Allowed' % request.method
    }
    return http.HttpResponse(status=405, content=template.render(RequestContext(request, model)))

def server_error(request):
    template = loader.get_template('error/default.html')
    model = {
        'status': 500,
        'exception': ''
    }
    return http.HttpResponseServerError(template.render(Context(model)))
