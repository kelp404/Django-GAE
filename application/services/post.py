from django.core.exceptions import PermissionDenied
from django.http import Http404
from application.models.datastore.post_model import *
from application.models.datastore.user_model import *
from application.models.dto.page_list import *
from application.middleware import g


class PostService(object):
    def get_posts(self, index, size):
        """
        Get posts.
        :param index: {int} The page index.
        :param size: {int} The page size.
        :return: PageList(PostModel)
        """
        posts = PostModel().all().order('-create_time').fetch(size, index * size)
        total = PostModel().all().count()
        return PageList(index, size, total, posts)

    def add_post(self, user_id, title, content):
        """
        Add a post.
        :param user_id: {long} The user id.
        :param title: The post title.
        :param content: The post content.
        :return: PostModel
        """
        if not g.request.user.is_login:
            raise PermissionDenied()

        # fetch author
        user = UserModel().get_by_id(user_id)

        post = PostModel()
        post.author = user
        post.title = title
        post.content = content
        post.put()
        post.get(post.key())
        return post

    def delete_post(self, post_id):
        """
        Delete the post.
        :param post_id: The post id.
        """
        if not g.request.user.is_login:
            raise PermissionDenied()

        post = PostModel().get_by_id(post_id)
        if post is None:
            raise Http404

        if g.request.user.permission != UserPermission.root and\
                        post.author.key().id() != g.request.user.id:
            raise PermissionDenied()

        post.delete()
        post.get(post.key())
