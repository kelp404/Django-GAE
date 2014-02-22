import unittest
from mock import MagicMock
from application.models.datastore.user_model import UserModel as User
from application.models.dto.page_list import *
from application.models.dto.user_model import *


class PageListTest(unittest.TestCase):
    def test_page_list_default(self):
        page_list = PageList()
        self.assertEqual(page_list.index, 0)
        self.assertEqual(page_list.size, 20)
        self.assertEqual(page_list.total, 0)

    def test_page_list_with_data(self):
        page_list = PageList(0, 10, 2, ['a', 'b'])
        self.assertListEqual(page_list, ['a', 'b'])

    def test_page_list_has_next_page(self):
        self.assertFalse(PageList().has_next_page)
        self.assertFalse(PageList(0, 20, 20).has_next_page)
        self.assertTrue(PageList(0, 20, 21).has_next_page)

    def test_page_list_has_previous_page(self):
        self.assertFalse(PageList().has_previous_page)
        self.assertTrue(PageList(1, 10, 11).has_previous_page)

    def test_page_list_max_index(self):
        self.assertEqual(PageList().max_index, -1)
        self.assertEqual(PageList(0, 10, 1).max_index, 0)
        self.assertEqual(PageList(0, 10, 11).max_index, 1)
        self.assertEqual(PageList(0, 10, 20).max_index, 1)

    def test_page_list_dict(self):
        class cls(object):
            def __init__(self, name):
                self.name = name
            def dict(self):
                return self.__dict__
        page_list = PageList(0, 10, 2, [cls('a'), cls('b')])
        self.assertDictEqual(page_list.dict(), {
            'index': 0,
            'size': 10,
            'total': 2,
            'has_next_page': False,
            'has_previous_page': False,
            'max_index': 0,
            'items': [
                {
                    'name': 'a'
                },
                {
                    'name': 'b'
                }
            ]
        })

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
