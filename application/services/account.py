from google.appengine.api import users
from application.models.datastore.user_model import UserModel as User
from application.models.dto.user_model import *


class AccountService(object):
    def __register_user(self, google_user, permission=UserPermission.normal):
        """
        Register the user.
        :param google_user: The google.appengine.api.users.get_current_user().
        :param permission: The user's permission.
        :return: The datastore.user_model.UserModel object.
        """
        user = User()
        user.email = google_user.email().lower()
        user.name = google_user.nickname()
        user.permission = permission
        user.put()
        user.get(user.key())
        return user

    def authorization(self):
        """
        User Authorization.
        :returns: dto.UserModel
        """
        google_user = users.get_current_user()
        if not google_user:
            # didn't login with google account
            return UserModel()

        if User.all().count(1) == 0:
            # set up default user with google account
            user = self.__register_user(google_user, UserPermission.root)
            return UserModel(user)

        if google_user:
            # auth with google account
            members = User.gql('where email = :1', google_user.email().lower()).fetch(1)
            if len(members) > 0:
                # got the user
                return UserModel(members[0])
            else:
                # register a new user
                user = self.__register_user(google_user)
                return UserModel(user)

        return UserModel()
