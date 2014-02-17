import json
from django.http import HttpResponse


class JsonResponse(HttpResponse):
    def __init__(self, content, *args, **kwargs):
        super(JsonResponse, self).__init__(json.dumps(content), content_type='application/json', *args, **kwargs)
