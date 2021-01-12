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
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView, name="index"),
    path('forum/', HomeView.as_view(), name="home"),
    path('forum/article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('forum/post/', AddPostView.as_view(), name="add-post"),
    path('forum/article/edit/<int:pk>', UpdatePostView.as_view(), name="update-post"),
    path('forum/article/<int:pk>/delete', DeletePostView.as_view(), name="delete-post"),
    path('forum/article/<int:pk>/comment/', AddCommentView.as_view(), name="add-comment"),
    path('forum/category/<str:cat>/', CategoryView, name="category"),
    path('forum/like/<int:pk>', LikeView, name="like-post"),
    path('spells/', SpellsView, name="spells_v"),
    path('spells/add', CreateSpellsView.as_view(), name="cr_spells_v"),
    path('spells/<int:pk>/delete', DeleteSpellsView.as_view(), name="del_spells_v"),
    path('feats/', FeatsView, name="feats_v"),
    path('feats/add', CreateFeatsView.as_view(), name="cr_feats_v"),
    path('feats/<int:pk>/delete', DeleteFeatsView.as_view(), name="del_feats_v"),
    path('races/', RacesView, name="races_v"),
    path('races/add', CreateRacesView.as_view(), name="cr_races_v"),
    path('races/<int:pk>/delete', DeleteRacesView.as_view(), name="del_races_v"),
    path('classes/', ClassesView, name="classes_v"),
    path('classes/add', CreateClassesView.as_view(), name="cr_classes_v"),
    path('classes/<int:pk>/delete', DeleteClassesView.as_view(), name="del_classes_v"),
    path('classes/<int:pk>/update', UpdateClassesView.as_view(), name="up_classes_v"),
    path('journals/', JournalsView, name="journals_v"),
    path('journals/add', CreateJournalsView.as_view(), name="cr_journals_v"),
    path('journals/<int:pk>/update', UpdateJournalsView.as_view(), name="up_journals_v"),
    path('journals/<int:pk>/delete', DeleteJournalsView.as_view(), name="del_journals_v"),
    path('journals/<int:pk>/posts', DetailJournalsView, name="det_journal"),
    path('journals/<int:pk>/posts/post', CreateJournalPostsView.as_view(), name="cr_journalpost_v"),
    path('journals/<int:jpk>/posts/<int:pk>/edit', UpdateJournalPostsView.as_view(), name="up_journalpost_v"),
    path('journals/<int:jpk>/posts/<int:pk>/delete', DeleteJournalPostsView.as_view(), name="del_journalpost_v"),
    path('characters/', CharactersView, name="characters_v"),
    path('characters/<int:pk>', DetailCharactersView.as_view(), name="det_characters_v"),
    path('characters/add', CreateCharactersView.as_view(), name="cr_characters_v"),
    path('characters/<int:pk>/delete', DeleteCharactersView.as_view(), name="del_characters_v"),
    path('characters/<int:pk>/update', UpdateCharactersView.as_view(), name="up_characters_v"),
]
