from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .tags.tag_service import create_tag_service

from .category.category_service import create_category_service

from .posts.post_service import create_post_service

# Create your views here.

@api_view(['POST'])
def create_post_view(request):

    try:
        response_data = create_post_service(request.data)
        return Response(response_data,status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def create_category_view(request):

    try:
        response_data = create_category_service(request.data)
        return Response(response_data,status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_tag_view(request):

    try:
        response_data = create_tag_service(request.data)
        return Response(response_data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'errror': str(e)}, status=status.HTTP_400_BAD_REQUEST)
