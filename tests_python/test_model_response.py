import unittest
from application.models.responses import *


class TestErrorViewModel(unittest.TestCase):
    def test_json_response_dict(self):
        response = JsonResponse({'x': True})
        self.assertEqual(response.content, '{"x": true}')

    def test_json_response_object(self):
        class TestClass(object):
            def __init__(self):
                self.x = 'x'
            def dict(self):
                return {
                    'x': self.x
                }
        response = JsonResponse(TestClass())
        self.assertEqual(response.content, '{"x": "x"}')
