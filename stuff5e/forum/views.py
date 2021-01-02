from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

class IndexView(ListView):
    model = Post
    template_name = 'index.html'

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