from user_profile.models import Post, Comment


def create_post(owner_id, author_id, msg):
    post = Post(owner_id=owner_id, author_id=author_id, message=msg)
    post.save()
    return post


def get_posts(user_id):
    comments = Comment.objects.all().select_related('post')
    print(comments)
    posts = Post.objects.filter(owner_id=user_id).order_by('-created_at')
    data = []
    for post in posts:
        data.append({
            'post': post,
            'comments': Comment.objects.filter(post_id=post.id).select_related('author')
        })
    return data
