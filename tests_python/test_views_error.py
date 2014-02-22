# -*- coding: utf-8 -*-

import unittest
from mock import MagicMock, patch
from application.models.view_model.error_model import *


class TestErrorViews(unittest.TestCase):
    def setUp(self):
        # mock django.template.RequestContext
        self.patchers = [
            patch('django.template.RequestContext', new=MagicMock()),
            patch('django.template.Context', new=MagicMock()),
        ]
        for patcher in self.patchers:
            patcher.start()

    def tearDown(self):
        for patcher in self.patchers:
            patcher.stop()

    def test_error_view(self):
        from application.views import error
        from django.template import RequestContext, Context
        request = MagicMock()
        request.method(return_value='/x')

        # bad request
        error.bad_request(request)
        RequestContext.assert_called_with(request, ErrorViewModel(
            status=400,
            exception='Bad Request'
        ))

        # permission denied
        error.permission_denied(request)
        RequestContext.assert_called_with(request, ErrorViewModel(
            status=403,
            exception='Permission Denied'
        ))

        # page not found
        error.page_not_found(request)
        RequestContext.assert_called_with(request, ErrorViewModel(
            status=404,
            exception='%s Not Found' % request.path
        ))

        # method not allowed
        error.method_not_allowed(request)
        RequestContext.assert_called_with(request, ErrorViewModel(
            status=405,
            exception='%s Not Allowed' % request.method
        ))

        # server error
        error.server_error(request)
        Context.assert_called_with(ErrorViewModel(
            status=500,
            exception='這一定是宿命'
        ))
