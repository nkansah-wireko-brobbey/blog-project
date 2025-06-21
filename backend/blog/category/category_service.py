
from .category_serializer import CategorySerializer
from rest_framework.exceptions import ValidationError


def create_category_service(data):
    serializer = CategorySerializer(data=data)
    
    if not serializer.is_valid():
        raise ValidationError(serializer.errors)

    serializer.save()
    
    return serializer.data
