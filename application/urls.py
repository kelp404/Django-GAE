from django.conf.urls import patterns, url
from application.views.home import *
from application.views.error import *


# error handlers
handler404 = page_not_found
handler405 = method_not_allowed
handler500 = server_error


# methods
def dispatch(**dispatches):
    def wraps(request, *args, **kwargs):
        handler = dispatches.get(request.method, lambda x: handler405(request))
        return handler(request, *args, **kwargs)
    return wraps


# routers
urlpatterns = patterns('',
    url(r'^$', dispatch(GET=home_view)),
)
