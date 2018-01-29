from user_profile.models import Post, Comment


def create_post(owner_id, author_id, msg):
    post = Post(owner_id=owner_id, author_id=author_id, message=msg)
    post.save()
    return post


def get_posts(user_id):
    posts = Post.objects.filter(owner_id=user_id).order_by('-created_at')
    posts_id = list(map(lambda p: p.id, posts))
    comments = Comment.objects.filter(post_id__in=posts_id)
    data = []
    for post in posts:
        data.append({
            'post': post,
            'comments': list(filter(lambda comment: comment.post_id == post.id, comments))
        })
    print(data)
    return data
