from application.models.datastore.post_model import *
from application.models.datastore.user_model import *


class PostService(object):
    def get_posts(self, index, size):
        return PostModel().all().order('create_time').fetch(size, index * size)

    def add_post(self, user_id, title, content):
        # fetch author
        user = UserModel().get_by_id(user_id)

        post = PostModel()
        post.author = user
        post.title = title
        post.content = content
        post.put()
        post.get(post.key())
        return post
