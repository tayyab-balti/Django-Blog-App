from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm, SignUpForm
import markdown as md  # Used to convert markdown text into HTML
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after signup
            return redirect('blog:post_list')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

# Show a list of published blog posts
@login_required
def post_list(request):
    # Get all posts that have a published_date in the past or now, sorted newest first
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    
    # Convert the post text from Markdown to HTML
    for post in posts:
        post.text = md.markdown(post.text)
    
    # Render them in the post_list.html template
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def my_blog_posts(request):
    posts = Post.objects.filter(author=request.user).order_by('-published_date')
    return render(request, 'blog/my_blog_posts.html', {'posts': posts})

# Show a single blog post and its comments
@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Get the post or return 404 if not found
    post.text = md.markdown(post.text)     # Convert Markdown to HTML
    comments = post.comments.all()         # Get all comments linked to the post
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})

# Create a new blog post
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)   # Create post but don't save yet
            post.author = request.user       # Set current user as author
            post.save()                      # Save to database
            post.publish()  # ✅ this sets published_date = timezone.now()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()  # Show an empty form if it's a GET request
    return render(request, 'blog/post_edit.html', {'form': form})

# Edit an existing blog post
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Get post or return 404
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            post.publish()  # ✅ this sets published_date = timezone.now()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)  # Pre-fill form with current post data
    return render(request, 'blog/post_edit.html', {'form': form, 'post': post})

# Delete a blog post
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()  # Delete the post
        return redirect('blog:post_list')  # Redirect to post list after deletion

# Add a comment to a specific post
@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  # Don’t save yet
            comment.post = post                # Link comment to post
            comment.author = request.user  # ✅ store the actual User object, not just username
            comment.save()                     # Save to database
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = CommentForm()  # Show empty comment form

    # ✅ ALWAYS pass the post, even on invalid form submission
    return render(request, 'blog/add_comment.html', {'form': form, 'post': post})

@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if comment.author != request.user:
        return redirect('blog:post_detail', pk=comment.post.pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/edit_comment.html', {'form': form, 'comment': comment})


@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if comment.author == request.user:
        comment.delete()

    return redirect('blog:post_detail', pk=comment.post.pk)

