import unittest
from datetime import datetime
from mock import MagicMock, patch
from google.appengine.ext import db
from application.models.datastore.post_model import *

class TestPostModel(unittest.TestCase):
    def test_post_model_properties(self):
        # mock google.appengine.ext.db
        self.patchers = [
            patch('google.appengine.ext.db.StringProperty.validate', new=MagicMock(return_value='StringProperty')),
            patch('google.appengine.ext.db.TextProperty.validate', new=MagicMock(return_value='TextProperty')),
        ]
        for patcher in self.patchers:
            patcher.start()

        post = PostModel()
        self.assertEqual(post.title, 'StringProperty')
        self.assertEqual(post.content, 'TextProperty')
        self.assertTrue(isinstance(post.create_time, datetime))

        for patcher in self.patchers:
            patcher.stop()

    def test_post_model_dict(self):
        fake_key = MagicMock()
        fake_key.id.return_value = 100
        post = PostModel()
        post.key = MagicMock(return_value=fake_key)
        post.title = 'title'
        post.content = 'content'
        self.assertDictEqual(post.dict(), {
            'id': 100,
            'title': 'title',
            'content': u'content',
            'author': None,
            'create_time': post.create_time.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        })
