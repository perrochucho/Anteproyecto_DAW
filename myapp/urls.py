from django.urls import path
from django.contrib.auth.views import LoginView
from .views import home, upload_ebook, profile

urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload_ebook, name='upload_ebook'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('profile/', profile, name='profile'),
]
