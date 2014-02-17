import json
from django.http import HttpResponse


class JsonResponse(HttpResponse):
    def __init__(self, content, *args, **kwargs):
        if isinstance(content, dict) or isinstance(content, list) or isinstance(content, basestring):
            dict_content = content
        else:
            dict_content = content.dict()
        super(JsonResponse, self).__init__(json.dumps(dict_content), content_type='application/json', *args, **kwargs)

    # def __is_serializable(self, object):
    #     if object
