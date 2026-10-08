from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
# Create your views here.
from django.http import HttpResponseRedirect
from blog.models import Post, Comment, Category
from blog.forms import CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.core.paginator import Paginator


# ------------- Paginas principales (index, categorias y detalle)
def index(request):
    posts = Post.objects.all().order_by("-created_on")
    categories = Category.objects.all()
    context = {
        "posts": posts,
        "categories": categories
    }

    paginator = Paginator(posts, 5)
    
    page_number = request.GET.get("page")
    post = paginator.get_page(page_number)
    
    context["post"] = post
    return render(request, "blog/index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")

    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            "category": category,
            "page_obj": page_obj,
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

def delete_comment(request, comment_id):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect("blog_index")

    comment = get_object_or_404(Comment, pk=comment_id)
    post_pk = comment.post.pk
    comment.delete()
    return redirect("blog:blog_detail", pk=post_pk)

# ----------- Buscador ------------------

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
        {
            "results": results,
            "query": query,
        },
    )


# ---------- Sistema de Usuarios ------------------
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

