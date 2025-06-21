
from .tag_serializer import TagSerializer
from rest_framework.exceptions import ValidationError


def create_tag_service(data):
    
    serializer = TagSerializer(data=data)

    if not serializer.is_valid():
        raise ValidationError(serializer.errors)
    
    serializer.save()

    return serializer.data