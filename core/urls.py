from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('blog.urls')),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page="login"), name='logout'),
]
