"""stuff5e URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from .views import IndexView, AddCommentView, HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, CategoryView, LikeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name="index"),
    path('forum/', HomeView.as_view(), name="home"),
    path('forum/article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('forum/post/', AddPostView.as_view(), name="add-post"),
    path('forum/article/edit/<int:pk>', UpdatePostView.as_view(), name="update-post"),
    path('forum/article/<int:pk>/delete', DeletePostView.as_view(), name="delete-post"),
    path('forum/article/<int:pk>/comment/', AddCommentView.as_view(), name="add-comment"),
    path('forum/category/<str:cat>/', CategoryView, name="category"),
    path('forum/like/<int:pk>', LikeView, name="like-post"),
]
