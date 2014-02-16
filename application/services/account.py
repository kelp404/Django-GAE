from google.appengine.api import users
from application.models.datastore.user_model import UserModel as User
from application.models.dto.user_model import *


class AccountService(object):
    def authorization(self):
        """
        User Authorization.

        :returns: dto.UserModel
        """
        google_user = users.get_current_user()
        if google_user:
            google_user = google_user.email().lower()
        else:
            return UserModel()

        if User.all().count(1) == 0:
            # set up default user with google account
            user = User()
            user.email = google_user
            user.name = google_user
            user.permission = UserPermission.root
            user.put()
            user.get(user.key())    # sync
            return UserModel(user)

        if google_user:
            # auth with google account
            members = User.gql('where email = :1', google_user).fetch(1)
            if len(members) > 0:
                return UserModel(members[0])

        return UserModel()
