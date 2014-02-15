from django.conf.urls import patterns, url
from application.views.home import *


urlpatterns = patterns('',
    url(r'^$', home_view)
)
