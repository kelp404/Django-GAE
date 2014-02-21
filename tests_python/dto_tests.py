import unittest
from mock import MagicMock
from application.models.datastore.user_model import UserModel as User
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
        users.create_logout_url = MagicMock(return_value='logout_url')

    def test_user_model_default(self):
        model = UserModel()
        self.assertFalse(model.is_login)
        self.assertEqual(model.id, 0)
        self.assertEqual(model.permission, UserPermission.anonymous)
        self.assertEqual(model.name, 'Guest')
        self.assertEqual(model.email, '')
        self.assertEqual(model.login_url, 'login_url')

    def test_user_model_with_data(self):
        fake_key = MagicMock()
        fake_key.id.return_value = 100
        user = User()
        user.name = 'name'
        user.email = 'email@gmail.com'
        user.key = MagicMock(return_value=fake_key)

        model = UserModel(user)
        self.assertEqual(model.id, 100)
        self.assertEqual(model.permission, UserPermission.normal)
        self.assertEqual(model.name, 'name')
        self.assertEqual(model.email, 'email@gmail.com')
        self.assertEqual(model.logout_url, 'logout_url')
