from django.shortcuts import render , redirect, reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy

from .forms import NewPostForm
from .models import Post


# def post_list_view(request):
#     all_post = Post.objects.filter(status='pub').order_by('-datetime_modified')
#     return render(request, 'blogfa/post_list.html', {'all_post': all_post})

class PostListview(generic.ListView):
    template_name = 'blogfa/post_list.html'
    context_object_name = 'all_post'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_modified')

# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blogfa/post_detail.html', {'post': post})


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blogfa/post_detail.html'
    context_object_name = 'post'


# def post_create_view(request):
#     if request.method == 'POST':
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')
#     else:
#         form = NewPostForm()
#     return render(request, 'blogfa/post_create.html', context={'form': form})

class PostCreatView(generic.CreateView):
    form_class = NewPostForm
    template_name = 'blogfa/post_create.html'
    context_object_name = 'form'


# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = NewPostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('post_list')
#
#     return render(request, 'blogfa/post_create.html', context={'form': form})


class PostUpdateView(generic.UpdateView):
    form_class = NewPostForm
    template_name = 'blogfa/post_create.html'
    model = Post


# def post_delete_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     if request.method == 'POST':
#         post.delete()
#         return redirect('post_list')
#
#     return render(request, 'blogfa/post_delete.html', context={'post': post})

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blogfa/post_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post_list')






