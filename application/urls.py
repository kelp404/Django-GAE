from django.conf.urls import patterns, url
from application.views.base import *
from application.views.error import *
from application.handlers.post import *


# error handlers
handler403 = permission_denied
handler404 = page_not_found
handler405 = method_not_allowed
handler500 = server_error


# methods
def dispatch(**dispatches):
    def wraps(request, *args, **kwargs):
        handler = dispatches.get(request.method, handler405)
        return handler(request, *args, **kwargs)
    return wraps
def api_dispatch(**dispatches):
    def wraps(request, *args, **kwargs):
        if 'application/json' not in request.META['HTTP_ACCEPT'].split(','):
            # return base view for first loading
            return base_view(request)
        handler = dispatches.get(request.method, handler405)
        return handler(request, *args, **kwargs)
    return wraps


# routers
urlpatterns = patterns('',
    url(r'^$', dispatch(GET=base_view)),
    url(r'^posts$', api_dispatch(GET=get_posts, POST=add_post)),
)
