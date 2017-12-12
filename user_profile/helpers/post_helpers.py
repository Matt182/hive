from user_profile.models import Post


def create_post(owner_id, author_id, msg):
    post = Post(owner_id=owner_id, author_id=author_id, message=msg)
    post.save()
    return post
