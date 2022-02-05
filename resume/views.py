from multiprocessing import context
from django.shortcuts import render
from django.views.generic import ListView
from .models import Resume, Post

# Create your views here.


def home(request):
    context = {
        'post':Resume.objects.get(pk=1)
    }
    return render(request, 'resume/home.html', context)


def about(request):
    resume = Resume.objects.get(pk=1)
    return render(request, 'resume/about.html', {'resume':resume})


def portfolio(request):
    return render(request, 'resume/portfolio.html')
    

def blog(request):
    posts = Post.objects.all()
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        posts = Post.objects.filter(title__icontains=item_name)
        
    return render(request, 'resume/blog.html', {'posts':posts})


# class PostlListView(ListView):
#     # model = Post
#     # ordering = ['-date']

#     # On peut juste utiliser cette ligne de code qui equivaut au deux lignes de code ci dessus
#     queryset = Post.objects.order_by('-date')
#     template_name = "resume/blog.html"
#     context_object_name = 'posts'


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'resume/post-detail.html', {'post':post})


def contact(request):
    return render(request, 'resume/contact.html')