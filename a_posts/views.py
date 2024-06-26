from django import forms
from django.shortcuts import redirect, render
from .models import *
from django.forms import ModelForm

def home_view(request):
    posts = Post.objects.all()
    return render(request, 'a_posts/home.html', {'posts': posts})

##function should be wriiten with smallletter starting and using underscore

class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        labels = {
            'body': 'caption',
        }
        widgets = {
    'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a caption ....', 'class': 'font1 text-4xl'})
}

def post_create_view(request):
    form = PostCreateForm() ## class should be written in camelcase

    if request.method == 'POST':
        form = PostCreateForm(request.POST)

        if form.is_valid:
            form.save()
            return redirect('home')
    return render(request, 'a_posts/post_create.html', {'form': form})

