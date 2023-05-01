from django.db import models
from django.contrib.auth.models import User

class Ebook(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    file = models.FileField(upload_to='ebooks')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ebooks = models.ManyToManyField(Ebook, blank=True)