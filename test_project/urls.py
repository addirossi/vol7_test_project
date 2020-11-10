"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from blog.views import index_page, posts_list, post_details, add_post, edit_post, delete_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='index-page'),
    # path('categories/<slug:slug>/', category_details, name='category-details'),
    path('posts/', posts_list, name='posts-list'),
    path('posts/<int:pk>/', post_details, name='post-details'),
    path('posts/add/', add_post, name='add-post'),
    path('posts/update/<int:pk>/', edit_post, name='edit-post'),
    path('posts/delete/<int:pk>/', delete_post, name='delete-post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 127.0.0.1:8000/posts - все посты
# 127.0.0.1:8000/posts/?category=slug - посты по определённой категории
