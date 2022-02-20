from django.shortcuts import render, HttpResponse
from .models import post

# Create your views here.
def list_blog(request):
    queryset = post.objects.filter(status=1).order_by('-Created_on')

    return render(request, 'main templete.html', {'content':queryset, 'title':"Articles"})

def blogpost(requests, blog_slug):
    obj = post.objects.get(slug=blog_slug)
    context = {'title': obj.Heading, 'content': obj.Content, 'author': obj.Author, 'date':obj.Created_on}

    return render(requests, 'blog_templete.html', context)
