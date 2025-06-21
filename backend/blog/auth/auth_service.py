
from .serializers import UserRegistrationSerializer
from rest_framework.exceptions import ValidationError


def register_service(data):

    serializer = UserRegistrationSerializer(data=data)

    if not serializer.is_valid():
        raise ValidationError(serializer.errors) 
    
    serializer.save()
    
    return serializer.data 
