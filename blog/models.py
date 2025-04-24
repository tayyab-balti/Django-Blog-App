from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# A model representing a blog post
class Post(models.Model):
    # Links the post to a user (author); deletes post if user is deleted
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # Title of the blog post (max 200 characters)
    title = models.CharField(max_length=200)
    
    # Main content of the post
    text = models.TextField()
    
    # Automatically sets to current time when the post is created
    created_date = models.DateTimeField(default=timezone.now)
    
    # Time when the post is published (can be empty)
    published_date = models.DateTimeField(null=True, blank=True)

    # Custom method to publish the post (sets the published date and saves)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # String representation (e.g., in admin panel)
    def __str__(self):
        return self.title

# A model representing a comment on a blog post
class Comment(models.Model):
    # Links comment to a post; deletes comment if post is deleted
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    
    # Author name of the comment 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # The comment text/content
    text = models.TextField()
    
    # Automatically sets to current time when the comment is created
    created_date = models.DateTimeField(default=timezone.now)

    # String representation
    def __str__(self):
        return self.text
