import threading
from application.services.account import AccountService


g = threading.local()

class AuthenticationMiddleware(object):
    def process_request(self, request):
        acs = AccountService()
        request.user = acs.authorization()

class GlobalMiddleware(object):
    def process_request(self, request):
        g.request = request
