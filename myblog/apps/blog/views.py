from django.shortcuts import render
from .models import Category; #(2),
from .models import Post; #(1),
# Create your views here.

#------Main page------#(1)
def index(request):
    context = {};
    posters = Post.objects.all();
    context['posters'] = posters;
    return render(request, "blog/index.html", context);

#------category page------#(2)
def category(request):
    context = {};
    categories = Category.objects.all();
    context['categories'] = categories;

    return render(request, "blog/category.html", context);

#------Blog page------#(1)
def blog(request):
    context = {};
    posters = Post.objects.filter(type = 'B');
    context['posters'] = posters;

    return render(request, "blog/blog.html", context);

#------tutorial page------#(1)
def tutorial(request):
    context = {};
    posters = Post.objects.filter(type = 'T');
    context['posters'] = posters;

    return render(request, "blog/tutorial.html", context);

#------contact page------#
def contact(request):
    context = {};
    return render(request, "blog/contact.html", context);
