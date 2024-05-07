from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import CreatePostForm, UpdatePostForm

def home(request):

    return render(request, 'fusionapp/index.html')

# Register
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'fusionapp/register.html', context=context)


# Login
def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('feed')
            else:
                return redirect('register', {'error': 'User not found'})

    context = {'form': form}
    return render(request, 'fusionapp/login.html', context = context)

# Logout
def logout(request):
    auth.logout(request)
    return redirect("login")

# Feed page
@login_required(login_url='login')
def feed(request):
    posts = Post.objects.all()
    context = {'posts': posts}

    return render(request, 'fusionapp/feed.html', context=context)


# Create
@login_required(login_url='login')
def create_post(request):
    form = CreatePostForm()
    

    if request.method == 'POST':

        form = CreatePostForm(request.POST)
        form.instance.author = request.user

        if form.is_valid():
            form.save()
            return redirect('feed')
        
    context = {'form': form}
    return render(request, 'fusionapp/create-post.html', context = context)

# Update
@login_required(login_url='login')
def update_post(request, pk):
    post = Post.objects.get(id=pk)
    form = UpdatePostForm(instance=post)

    if request.method == 'POST':
        form = UpdatePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('feed')

    context = {'form': form}
    return render(request, 'fusionapp/update-post.html', context=context)

# Delete
@login_required(login_url='login')
def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('feed')

#View Post
@login_required(login_url='login')
def view_post(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'fusionapp/view-post.html', context=context)


#User Profile
@login_required(login_url='login')
def user_profile(request):
    user = request.user
    posts = Post.objects.filter(author=user)
    context = {'posts': posts}
    return render(request, 'fusionapp/user-profile.html', context=context)


