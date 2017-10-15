from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import SignUpForm
from .models import Post, Comment, Profile

def index(request):
    if request.user.is_authenticated():
        all_users = User.objects.all()#väliaikainen!11
        profile = Profile.objects.get(user=request.user)
        latest_posts = Post.objects.all().order_by('-date')
        context = {"latest_posts": latest_posts, "profile":profile, "all_users":all_users}
        return render(request, "app/index.html", context)
    else:
        return render(request, "app/index.html")


def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    profile = Profile.objects.get(user=user)
    posts = Post.objects.filter(user_name=profile).order_by('-id')
    #----------Followers/Followings-----------
    followed_user_list = []
    follower_user_list = []
    for followed_user_id in profile.following:
        for followed_user in User.objects.all():
            if followed_user_id == followed_user.id:
                followed_user_list.insert(0, followed_user)

    for follower_user_id in profile.followers:
        for follower_user in User.objects.all():
            if follower_user_id == follower_user.id:
                follower_user_list.insert(0, follower_user)
    #---------Liked posts--------
    liked_posts_img_list = []
    for liked_post_id in profile.liked_post_list:
        for post in Post.objects.all():
            if liked_post_id == post.id:
                liked_posts_img_list.insert(0, post)
    context = {"user_profile":profile, "posts": posts, "followed_user_list": followed_user_list, "follower_user_list":follower_user_list, "liked_posts_img_list":liked_posts_img_list}
    return render(request, "app/profile.html", context)

def display_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {"post":post}
    return render(request, "app/post.html", context)


def explore(request):
    posts = Post.objects.all()
    context = {"posts":posts}
    return render(request, "app/explore.html", context)

#-----------------------Toiminnot----------------------

def post_view(request):
    if request.method == 'POST' and request.FILES['image']:
        u = User.objects.get(pk=request.user.id)
        user = Profile.objects.get(user=u)
        text = request.POST['text']
        img = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        uploaded_file_url = fs.url(filename)
        next = request.POST.get('next', '/')
        post = Post.objects.create(user_name=user, text=text, img=img)
        post.save()
    return HttpResponseRedirect(next)

def post_comment(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(pk=post_id)
        u = User.objects.get(pk=request.user.id)
        user = Profile.objects.get(user=u)
        comment = request.POST['comment']
        post.comment_set.create(post=post, user_name=user, text=comment)
        next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            messages.success(request, 'Signup successful!', extra_tags="alert-success text-center")
            return redirect('../')
    else:
        form = SignUpForm()
    return render(request, 'app/signup.html', {'form': form})

def init_profile(request):
    if request.method == 'POST' and request.FILES['image']:
        img = request.FILES['image']
        bio = request.POST['bio']
        location = request.POST['location']
        birth_date = request.POST['birth_date']
        user = User.objects.get(pk=request.user.id)
        profile = Profile.objects.get(user=user)
        profile.pic = img
        profile.bio = bio
        profile.location = location
        profile.birth_date = birth_date
        profile.save()
        return redirect("../")

def update_profile(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user = User.objects.get(pk=user_id)
        profile = Profile.objects.get(user=user)
        bio = request.POST['bio']
        location = request.POST['location']
        birth_date = request.POST['birth_date']
        profile.bio = bio
        profile.location = location
        profile.birth_date = birth_date
        profile.save()
    return redirect("../../user/"+user_id)


def like(request, post_id):
    this_post = Post.objects.get(pk=post_id)
    user = User.objects.get(pk=request.user.id)
    next = request.POST.get('next', '/')
    if this_post.id not in user.profile.liked_post_list:
        this_post.likes += 1
        this_post.save()
        user.profile.liked_post_list.append(post_id)
        user.profile.save()
    else:
        this_post.likes -= 1
        this_post.save()
        user.profile.liked_post_list.remove(this_post.id)
        user.profile.save()
    return HttpResponseRedirect(next)


def follow(request, user_id):
    user_to_follow = User.objects.get(pk=user_id)
    profile = Profile.objects.get(user=request.user)
    if user_to_follow.id not in profile.following and user_to_follow.id is not request.user.id:
        profile.following.append(user_to_follow.id)
        profile.save()
        user_to_follow.profile.followers.append(request.user.id)
        user_to_follow.profile.save()
    elif user_to_follow.id in profile.following:
        profile.following.remove(user_to_follow.id)
        profile.save()
        user_to_follow.profile.followers.remove(request.user.id)
        user_to_follow.profile.save()
    return redirect("../../user/"+user_id)



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!', extra_tags="alert-success text-center")
            if not user.profile.pic:
                no_profile = True
                return render(request, "app/header.html", {"no_profile":no_profile})
            else:
                return redirect("../")
        else:
            messages.warning(request, 'Username or password is incorrect!', extra_tags="alert-danger text-center")
            return redirect("../")

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout successful!', extra_tags="alert-success text-center")
    return redirect("../")
