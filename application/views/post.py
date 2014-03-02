import json
from django.http import HttpResponse
from application.decorators import *
from application.exceptions import Http400
from application.services.post import *
from application.models.responses import JsonResponse


def get_posts(request):
    """
    Get posts.
    :param request.GET:
        index: The page index.
    :return: JsonResponse([PostModel])
    """
    model = request.GET.dict()
    try:
        index = int(model.get('index', '0'))
    except:
        raise Http400

    ps = PostService()
    posts = ps.get_posts(index, 10)
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

@authorization(UserPermission.normal, UserPermission.root)
def delete_post(request, post_id):
    """
    Delete the post.
    :param post_id: The post id.
    """
    post_id = long(post_id)

    ps = PostService()
    ps.delete_post(post_id)
    return HttpResponse(status=200)
