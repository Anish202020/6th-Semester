from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
class PostListView(ListView):
 model = Post
 template_name = 'post_list.html' # default is 'blog/post_list.html'
 context_object_name = 'posts'
class PostDetailView(DetailView):
 model = Post
 template_name = 'post_detail.html' # default is 'blog/post_detail.html'
class PostCreateView(CreateView):
 model = Post
 template_name = 'post_form.html' # default is 'blog/post_form.html'
 fields = ['title', 'content']
class PostUpdateView(UpdateView):
 model = Post
 template_name = 'post_form.html'
 fields = ['title', 'content']
class PostDeleteView(DeleteView):
 model = Post
 template_name = 'post_confirm_delete.html' # default is 'blog/post_confirm_delete.html'
 success_url = '/'