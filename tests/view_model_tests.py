import unittest
from application.models.view_model.error_model import *


class ErrorViewModelTest(unittest.TestCase):
    def setUp(self):
        self.model = ErrorViewModel()

    def test_error_view_model_default(self):
        self.assertEqual(self.model.status, 0)
        self.assertEqual(self.model.exception, '')

    def test_error_view_model_init(self):
        self.model = ErrorViewModel(status=405, exception='msg')
        self.assertEqual(self.model.status, 405)
        self.assertEqual(self.model.exception, 'msg')

    def test_error_view_model_instance(self):
        self.assertTrue(isinstance(self.model, dict))

    def test_error_view_model_properties(self):
        self.model.status = 500
        self.model.exception = 'ex'
        self.assertEqual(self.model.status, 500)
        self.assertEqual(self.model.exception, 'ex')
