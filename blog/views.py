from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm 
from django.contrib.auth.decorators import login_required

class Index(ListView):
    model = Post
    #post = Post.objects.all().order_by('-date_posted')
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 1

class Featured(ListView):
    model = Post
    post = Post.objects.filter(featured=True).order_by('-date_posted')
    template_name = 'blog/featured.html'
    context_object_name = 'posts'
    paginate_by = 1

class DetailArticleView(DetailView):
    model = Post
    template_name = 'blog/post.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailArticleView, self).get_context_data(*args, **kwargs)
        context['liked_by_user'] = False
        post = Post.objects.get(id=self.kwargs.get('pk'))
        if post.likes.filter(pk=self.request.user.id).exists():
            context['liked_by_user'] = True
        return context


class LikePost(View):
    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        if post.likes.filter(pk=self.request.user.id).exists():
            post.likes.remove(request.user.id)
        else:
            post.likes.add(request.user.id)

        post.save()
        return redirect('detail_post', pk)

class BlogPostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post 
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('index')
    
    def text_func(self):
        post = Post.objects.get(id=self.kwargs.get('pk'))
        return self.request.user.id == post.author.id

    def get_queryset(self):
        return super().get_queryset()

@login_required
def create_blog_post(request):
    
    if request.method == 'POST':
         form = PostForm(request.POST)
         if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form =PostForm()

    return render(request, 'blog/create_blog.html', {'form': form})

@login_required
def task_update(request, id):
    post = get_object_or_404(Post, id=id)  
   

    if request.method == 'POST':
         form = PostForm(request.POST, instance=post)
         if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = PostForm(instance=post)

    return render(request, 'blog/update_blog.html', {'form': form})

    
    
