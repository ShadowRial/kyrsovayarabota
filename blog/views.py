from django.shortcuts import render
from .models import Post


def home(request):
    # context = {
    #     'posts': Post.objects.all()
    # }
    # в return , context
    return render(request, 'center/index.html')


def about(request):
    return render(request, 'center/about.html')

def contact(requst):
    return render(requst, 'center/contact.html')