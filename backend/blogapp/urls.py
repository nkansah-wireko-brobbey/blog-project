"""
URL configuration for blogapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from blog.views import MyTokenObtainPairView, create_post_view, create_tag_view, register_view
from blog.views import create_category_view

urlpatterns = [
    path("api/posts/", create_post_view),
    path("api/category/", create_category_view),
    path("api/tag/", create_tag_view),
    path("api/auth/register", register_view),
    path("api/auth/login", MyTokenObtainPairView.as_view()),
    path("admin/", admin.site.urls),
]
