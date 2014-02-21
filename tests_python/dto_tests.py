import unittest
from application.models.dto.user_model import *


class UserPermissionTest(unittest.TestCase):
    def test_user_permission(self):
        self.assertEqual(UserPermission.anonymous, 0)
        self.assertEqual(UserPermission.root, 1)
        self.assertEqual(UserPermission.normal, 2)
