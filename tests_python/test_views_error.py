import unittest
from mock import MagicMock, patch
from application.models.view_model.error_model import *


class TestErrorViews(unittest.TestCase):
    def setUp(self):
        # mock django.template.RequestContext
        self.patchers = [
            patch('django.template.RequestContext', new=MagicMock()),
        ]
        for patcher in self.patchers:
            patcher.start()

    def tearDown(self):
        for patcher in self.patchers:
            patcher.stop()

    def test_bad_request(self):
        from application.views.error import bad_request
        from django.template import RequestContext

        request = MagicMock()
        bad_request(request)
        RequestContext.assert_called_with(request, ErrorViewModel(
            status=400,
            exception='Bad Request'
        ))
