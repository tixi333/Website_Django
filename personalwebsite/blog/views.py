from django.shortcuts import render,redirect
from django.db.models import Q
# Create your views here.
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from blog.models import Post, Comment, Category
from blog.forms import CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

def index(request):
    posts = Post.objects.all().order_by("-created_on")
    categories = Category.objects.all()
    context = {
        "posts": posts,
        "categories": categories
    }
    
    return render(request, "blog/index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }
    return render(request, "blog/detail.html", context)

def blog_search(request):
    query = request.GET.get("q", "").strip()
    results = Post.objects.none()

    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query) | Q(categories__name__icontains=query)| Q(created_on__icontains=query) 
        ).distinct().order_by("-created_on")

    return render(
        request,
        "blog/search.html",
        {"results": results, "query": query},
    )


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("blog:index")
    else:
        form = UserCreationForm()

    return render(request, "blog/register.html", {"form": form})

def logout(request):
    logout(request)
    return redirect('home')