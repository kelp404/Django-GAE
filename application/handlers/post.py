import json
from application.decorators import *
from application.services.post import *
from application.responses import JsonResponse


def get_posts(request):
    model = request.GET
    ps = PostService()
    posts = ps.get_posts(
        index=int(model.get('index', ['0'])),
        size=int(model.get('size', ['20']))
    )
    result = [post.dict() for post in posts]
    return JsonResponse(result)

@authorization(UserPermission.normal, UserPermission.root)
def add_post(request):
    model = json.loads(request.body)
    ps = PostService()
    post = ps.add_post(request.user.id, model.get('title'), model.get('content'))
    return JsonResponse(post.dict())
