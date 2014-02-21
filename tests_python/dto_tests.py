import unittest
from mock import MagicMock
from application.models.dto.user_model import *


class UserPermissionTest(unittest.TestCase):
    def test_user_permission(self):
        self.assertEqual(UserPermission.anonymous, 0)
        self.assertEqual(UserPermission.root, 1)
        self.assertEqual(UserPermission.normal, 2)

class UserModelTest(unittest.TestCase):
    def setUp(self):
        # mock google.appengine.api.users
        from google.appengine.api import users
        users.create_login_url = MagicMock(return_value='login_url')

    def test_user_model_default(self):
        model = UserModel()
        self.assertFalse(model.is_login)
        self.assertEqual(model.id, 0)
        self.assertEqual(model.permission, UserPermission.anonymous)
        self.assertEqual(model.name, 'Guest')
        self.assertEqual(model.email, '')
        self.assertEqual(model.login_url, 'login_url')

