from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import AddPostForm, EditPostForm
from .models import Category, Post


# class IndexPageView(View):
#     def get(self):
#         queryset = Category.objects.all()
#         return render(self.request, 'blog/index.html', {'categories': queryset})


class IndexPageView(ListView):
    model = Category
    template_name = 'blog/index.html'
    context_object_name = 'categories'


class PostsListView(ListView):
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.request.GET.get('category')
        if category_slug is not None:
            queryset = queryset.filter(category_id=category_slug)
        return queryset


class PostDetailsView(DetailView):
    model = Post
    template_name = 'blog/post_details.html'
    context_object_name = 'post'


class AddPostView(CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    form_class = AddPostForm

    def form_valid(self, form):
        post = form.save()
        return redirect(post.get_absolute_url())


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'blog/edit_post.html'
    form_class = EditPostForm
    context_object_name = 'post'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('index-page')
