from django.shortcuts import redirect, render
from .models import Post
from django.contrib.auth.models import User
from .forms import PostForm, PostModelForm
import uuid


# Create your views here.
def list(request):
    posts = Post.objects.all()
    return render(request, "post/list.html", {"posts": posts})


def show(request, id):
    post = Post.objects.get(pk=id)
    return render(request, "post/show.html", {"post": post})


# Using regular form
# def upload_file(f):
#     path = "uploads/images/" + str(uuid.uuid4()) + ".png"
#     with open(path, "wb+") as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)
#     return path

# def create(request):
#     if request.method == "GET":
#         return render(request, "post/create.html", {"form": PostForm})
#     elif request.method == "POST":
#         form = PostForm(request.POST, request.FILES)
#         # form = PostForm(request.POST)
#         if form.is_valid():
#             path = upload_file(request.FILES["image"])
#             post = Post(
#                 title=form.cleaned_data["title"],
#                 content=form.cleaned_data["content"],
#                 is_published=form.cleaned_data["is_published"],
#                 image=path,
#             )
#             post.save()
#             user = form.cleaned_data["user"]
#             user.post_set.add(post)
#             post.tags.set(form.cleaned_data["tags"])
#             return redirect("list")


# Using model form
def create(request):
    if request.method == "GET":
        return render(request, "post/create.html", {"form": PostModelForm})
    elif request.method == "POST":
        form = PostModelForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("list")


# Using regular form
# def update(request, id):
#     post = Post.objects.get(pk=id)
#     if request.method == "GET":
#         return render(
#             request,
#             "post/update.html",
#             {
#                 "form": PostForm(
#                     initial={
#                         "title": post.title,
#                         "content": post.content,
#                         "image": post.image,
#                         "is_published": post.is_published,
#                         "user": post.user,
#                         "tags": post.tags.all,
#                     }
#                 ),
#                 "post": post,
#             },
#         )
#     elif request.method == "POST":
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             path = (
#                 upload_file(request.FILES["image"])
#                 if "image" in request.FILES
#                 else post.image
#             )
#             Post.objects.update_or_create(
#                 pk=id,
#                 defaults={
#                     "title": form.cleaned_data["title"],
#                     "content": form.cleaned_data["content"],
#                     "is_published": form.cleaned_data["is_published"],
#                     "image": path,
#                 },
#             )
#             user = form.cleaned_data["user"]
#             user.post_set.add(post)
#             post.tags.set(form.cleaned_data["tags"])
#             return redirect("list")


# Using model form
def update(request, id):
    post = Post.objects.get(pk=id)
    if request.method == "GET":
        return render(
            request,
            "post/update.html",
            {
                "form": PostModelForm(instance=post),
                "post": post,
            },
        )
    elif request.method == "POST":
        form = PostModelForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("list")
