from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uploaded_file = models.FileField(upload_to='uploaded_files/', null=True, blank=True)
