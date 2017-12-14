from user_profile.models import Comment


def create_comment(post_id, author_id, msg):
    comment = Comment(post_id=post_id, author_id=author_id, message=msg)
    comment.save()
    return comment
