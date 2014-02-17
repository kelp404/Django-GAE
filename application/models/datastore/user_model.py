from google.appengine.ext import db
from application.models.dto.user_model import UserPermission


class UserModel(db.Model):
    email = db.EmailProperty()
    name = db.StringProperty(indexed=False)
    permission = db.IntegerProperty(default=UserPermission.normal)
    create_time = db.DateTimeProperty(auto_now_add=True)

    def dict(self):
        return {
            'id': self.key().id(),
            'name': self.name,
            'email': self.email,
            'permission': self.permission,
            'create_time': self.create_time.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        }
