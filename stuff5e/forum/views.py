from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .filters import *
from django.db.models import Count

def SpellsView(request):
    spells = Spell.objects.all().order_by("custom","name")
    filter = SpellFilter(request.GET, queryset=spells)
    spells = filter.qs
    
    context = {'spells':spells,'filter':filter}
    return render(request, 'spells.html', context)
    
def FeatsView(request):
    feats = Feat.objects.all().order_by("custom","name")
    filter = FeatFilter(request.GET, queryset=feats)
    feats = filter.qs
    
    context = {'feats':feats,'filter':filter}
    return render(request, 'feats.html', context)
    
def RacesView(request):
    races = Race.objects.all().order_by("custom","name")
    filter = RaceFilter(request.GET, queryset=races)
    races = filter.qs
    
    context = {'races':races,'filter':filter}
    return render(request, 'races.html', context)

def ClassesView(request):
    classes = Class.objects.all().order_by("custom","name")
    filter = ClassFilter(request.GET, queryset=classes)
    classes = filter.qs
    
    context = {'classes':classes,'filter':filter}
    return render(request, 'classes.html', context)
    
def JournalsView(request):
    model = Journal.objects.all().order_by('title')
    journal_users = Journal.objects.annotate(Count('user_access'))
    journal_posts = Journal.objects.annotate(Count('journal_posts'))
    
    context = {'model':model, 'journal_users':journal_users, 'journal_posts':journal_posts}
    return render(request, 'journals.html', context)
    
def DetailJournalsView(request, pk):
    model = Journal.objects.filter(pk=pk).order_by('title')
    journal_users = Journal.objects.annotate(Count('user_access'))
    journal_posts = JournalPost.objects.filter(journal=pk)
    
    context = {'model':model, 'journal_users':journal_users, 'journal_posts':journal_posts}
    return render(request, 'journal_details.html', context)
    
    
def CharactersView(request):
    characters = Character.objects.all().order_by('name')
    
    context = {'characters':characters}
    return render(request, 'characters.html', context)

class DetailCharactersView(DetailView):
    model = Character   
    template_name = 'character_detail.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(DetailCharactersView, self).get_context_data(*args, **kwargs)

        return context
    
# ------------------------------------------ #

class UpdateClassesView(UpdateView):
    model = Class
    form_class = ClassForm
    template_name = 'update_class.html'
    success_url = reverse_lazy('classes_v')
    
class UpdateJournalsView(UpdateView):
    model = Journal
    form_class = JournalForm
    template_name = 'update_journals.html'
    success_url = reverse_lazy('journals_v')

class UpdateJournalPostsView(UpdateView):
    model = JournalPost
    form_class = JournalPostForm
    template_name = 'journal_post_update.html'
    success_url = reverse_lazy('journals_v')
    
    def get_context_data(self, *args, **kwargs):
        context = super(UpdateJournalPostsView, self).get_context_data(*args, **kwargs)
        
        context["model"] = Journal.objects.filter(pk=self.kwargs['jpk']).order_by('title')
        context["journal_users"] = Journal.objects.annotate(Count('user_access'))
        return context
    
class UpdateCharactersView(UpdateView):
    model = Character
    form_class = CharacterForm
    template_name = 'update_character.html'
    success_url = reverse_lazy('characters_v')
    
# ------------------------------------------ #

class CreateSpellsView(CreateView):
    model = Spell
    form_class = SpellForm
    template_name = 'create_spell.html'
    success_url = reverse_lazy('spells_v')
    
class CreateFeatsView(CreateView):
    model = Feat
    form_class = FeatForm
    template_name = 'create_feat.html'
    success_url = reverse_lazy('feats_v')
    
class CreateRacesView(CreateView):
    model = Race
    form_class = RaceForm
    template_name = 'create_race.html'
    success_url = reverse_lazy('races_v')

class CreateClassesView(CreateView):
    model = Class
    form_class = ClassForm
    template_name = 'create_class.html'
    success_url = reverse_lazy('classes_v')
    
class CreateJournalsView(CreateView):
    model = Journal
    form_class = JournalForm
    template_name = 'create_journal.html'
    success_url = reverse_lazy('journals_v')
    
class CreateJournalPostsView(CreateView):
    model = JournalPost
    form_class = JournalPostForm
    template_name = 'journal_post_add.html'
    success_url = reverse_lazy('journals_v')
    
    def form_valid(self, form):
        form.instance.journal_id = self.kwargs['pk']
        return super().form_valid(form)
        
    def get_context_data(self, *args, **kwargs):
        context = super(CreateJournalPostsView, self).get_context_data(*args, **kwargs)
        
        context["model"] = Journal.objects.filter(pk=self.kwargs['pk']).order_by('title')
        context["journal_users"] = Journal.objects.annotate(Count('user_access'))
        return context
    
class CreateCharactersView(CreateView):
    model = Character
    form_class = CharacterForm
    template_name = 'create_character.html'
    success_url = reverse_lazy('characters_v')
    
# ------------------------------------------ #

class DeleteSpellsView(DeleteView):
    model = Spell
    template_name = 'delete_spell.html'
    success_url = reverse_lazy('spells_v')
    
class DeleteFeatsView(DeleteView):
    model = Feat
    template_name = 'delete_feat.html'
    success_url = reverse_lazy('feats_v')
    
class DeleteRacesView(DeleteView):
    model = Race
    template_name = 'delete_race.html'
    success_url = reverse_lazy('races_v')

class DeleteClassesView(DeleteView):
    model = Class
    template_name = 'delete_class.html'
    success_url = reverse_lazy('classes_v')
    
class DeleteJournalsView(DeleteView):
    model = Journal
    template_name = 'delete_journal.html'
    success_url = reverse_lazy('journals_v')

class DeleteJournalPostsView(DeleteView):
    model = JournalPost
    template_name = 'journal_post_delete.html'
    success_url = reverse_lazy('journals_v')
    
    def get_context_data(self, *args, **kwargs):
        context = super(DeleteJournalPostsView, self).get_context_data(*args, **kwargs)
        
        context["model"] = Journal.objects.filter(pk=self.kwargs['jpk']).order_by('title')
        context["journal_users"] = Journal.objects.annotate(Count('user_access'))
        context["journal_posts"] = JournalPost.objects.filter(journal=self.kwargs['jpk'])
        context["todelete"] = JournalPost.objects.filter(pk=self.kwargs['pk'])
        return context
    
class DeleteCharactersView(DeleteView):
    model = Character
    template_name = 'delete_character.html'
    success_url = reverse_lazy('characters_v')
     
    
# ------------------------------------------ #
    
def IndexView(request):
    model = Post
    return render(request, 'index.html')

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

class ArticleDetailView(DetailView):
    model = Post    
    template_name = 'article_details.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        
        like_obj = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = like_obj.total_likes()
        context["total_likes"] = total_likes
        
        liked = False
        if like_obj.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["liked"] = liked
        
        return context
    
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('home',)

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
    success_url = reverse_lazy('home')
    
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    
class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
def CategoryView(request, cat):
    category_posts = Post.objects.filter(category=cat)
    return render(request, 'categories.html', {'cat':cat, 'posts':category_posts})
    
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post-id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))