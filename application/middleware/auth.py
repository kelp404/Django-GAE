from application.services.account_service import AccountService


class AuthenticationMiddleware(object):
    def process_request(self, request):
        acs = AccountService()
        request.user = acs.authorization()
