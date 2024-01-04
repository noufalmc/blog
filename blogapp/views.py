from django.shortcuts import render, redirect

from .models import blog
from .forms import CommentForms
from .models import comment as cm


# Create your views here.
def frontpage(request):
    posts = blog.objects.all()
    return render(request, 'blog/frontpage.html', {'posts': posts})


def detail(request, slug):
    detail = blog.objects.get(slug=slug)
    if request.method == 'POST':
        form = CommentForms(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = detail
            comment.save()
            return redirect('detail', slug=detail.slug)
    else:
        forms1 = CommentForms()

        return render(request, 'blog/detail.html', {'detail': detail, 'form': forms1})
