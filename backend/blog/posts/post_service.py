from ..models import Post
from .post_serializer import PostSerializer
from rest_framework.exceptions import ValidationError

def create_post_service(data, user=None):
    serializer = PostSerializer(data=data)
    if not serializer.is_valid():
        raise ValidationError(serializer.errors)
    if user:
        serializer.save(user=user)
    else:
        serializer.save()
    return serializer.data
