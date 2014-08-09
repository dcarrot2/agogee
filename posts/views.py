from django.shortcuts import render

from django.views.generic import ListView
from .models import Post, Vote

class PostListView(ListView):
    model = Post
    queryset = Post.with_votes.all()
    paginate_by = 3