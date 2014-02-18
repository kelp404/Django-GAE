import json
from application.decorators import *
from application.services.post import *
from application.responses import JsonResponse


def get_posts(request):
    """
    Get posts.
    :param request.GET:
        index: The page index.
        size: The page size.
    :return: JsonResponse([PostModel])
    """
    model = request.GET.dict()
    ps = PostService()
    posts = ps.get_posts(
        index=int(model.get('index', '0')),
        size=int(model.get('size', '10'))
    )
    return JsonResponse(posts)

@authorization(UserPermission.normal, UserPermission.root)
def add_post(request):
    """
    Add a post.
    :param request.body:
        It should be json.
        title: The post title.
        content The post content.
    :return: JsonResponse(PostModel)
    """
    model = json.loads(request.body)
    ps = PostService()
    post = ps.add_post(request.user.id, model.get('title'), model.get('content'))
    return JsonResponse(post.dict())
