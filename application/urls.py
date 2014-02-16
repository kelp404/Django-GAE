from django.conf.urls import patterns, url
from application.views.home import *
from application.views.error import *


# error handlers
handler404 = page_not_found


# routers
urlpatterns = patterns('',
    url(r'^$', home_view),
)
