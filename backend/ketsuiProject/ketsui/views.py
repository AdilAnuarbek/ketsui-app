from django.shortcuts import render

from ketsui.helper_functions import romaji_to_hiragana
from ketsui.models import Post

# Create your views here.

def index(request):
    context = {}
    return render(request, "index.html", context)

def post_list(request):
    posts = Post.objects.all().order_by('-created_at') # Get all posts, newest first
    context = {'posts': posts}
    return render(request, 'post_list.html', context)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug) # Get the specific post
    context = {'post': post}
    return render(request, 'post_detail.html', context)

def hiragana_table(request):
    context = {}
    return render(request, 'hiragana/hiragana.html', context)

def hiragana_kana(request, kana):
    context = {'kana': {
        'romaji': kana,
        'hiragana': romaji_to_hiragana(kana),
    }}
    return render(request, 'hiragana/kana.html', context)