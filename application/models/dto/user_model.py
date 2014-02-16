

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
        else:
            self.is_login = True
            self.id = user_data.key().id()
            self.permission = user_data.permission
            self.name = user_data.name
            self.email = user_data.email
