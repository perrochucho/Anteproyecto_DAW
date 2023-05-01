from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Ebook
from .forms import EbookForm, LoginForm

def home(request):
    if request.user.is_authenticated:
        ebooks = request.user.userprofile.ebooks.all()
        return render(request, 'home.html', {'ebooks': ebooks})
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})

@login_required
def upload_ebook(request):
    if request.method == 'POST':
        form = EbookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '¡El libro electrónico se ha subido con éxito!')
            return redirect('home')
    else:
        form = EbookForm()
    return render(request, 'upload_ebook.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html')
