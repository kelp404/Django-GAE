from google.appengine.ext import db
from .user_model import *


class PostModel(db.Model):
    title = db.StringProperty(indexed=False)
    content = db.TextProperty()
    author = db.ReferenceProperty(reference_class=UserModel)
    create_time = db.DateTimeProperty(auto_now_add=True)

    def dict(self):
        result = {
            'id': self.key().id(),
            'title': self.title,
            'content': self.content,
            'author': self.author.dict(),
            'create_time': self.create_time.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        }
        return result