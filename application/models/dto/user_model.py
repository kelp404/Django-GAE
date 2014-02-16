from google.appengine.api import users


class UserPermission(object):
    anonymous = 0
    root = 1
    normal = 2

class UserModel(object):
    def __init__(self, user_data=None):
        if user_data is None:
            self.is_login = False
            self.id = 0
            self.permission = UserPermission.anonymous
            self.name = 'Guest'
            self.email = ''
            self.login_url = users.create_login_url()
        else:
            self.is_login = True
            self.id = user_data.key().id()
            self.permission = user_data.permission
            self.name = user_data.name
            self.email = user_data.email
            self.logout_url = users.create_logout_url('/')
