
from .category_serializer import CategorySerializer


def create_category_service(data):
    serializer = CategorySerializer(data=data)

    if serializer.is_valid():
        serializer.save()
    
    return serializer.data
