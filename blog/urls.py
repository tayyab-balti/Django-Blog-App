from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    # Singup 
    path("signup/", views.signup_view, name='signup'),
    
    # Post URLs
    path("", views.post_list, name='post_list'),
    path("blog/my-post/", views.my_blog_posts, name='my_blog_posts'),
    path("post/new/", views.post_new, name='post_new'),
    path("post/<int:pk>/", views.post_detail, name='post_detail'),
    path("post/<int:pk>/edit/", views.post_edit, name='post_edit'),
    path("post/<int:pk>/delete/", views.post_delete, name='post_delete'),

    # Comment URLs
    path("post/<int:pk>/comment/", views.add_comment, name='add_comment'),
    path("comment/<int:pk>/edit/", views.edit_comment, name='edit_comment'),
    path("comment/<int:pk>/delete/", views.delete_comment, name='delete_comment'),
]