from django.shortcuts import render, redirect, get_object_or_404;
from django.core.exceptions import ObjectDoesNotExist;
from .models import Category; #(2),
from .models import Post; #(1),
# Create your views here.

#------Main page------#(1)
def index(request):
    context = {};
    posters = Post.objects.filter(state = True)[::-1]; #this form flips the list;
    context['posters'] = posters;
    return render(request, "blog/index.html", context);

#------category page------#(2),(1)
def category(request, category_name = None):
    # print(category_name);
    context = {};

    if category_name == None:
        categories = Category.objects.all();
        context['categories'] = categories;
    else:
        try:
            # if exist slug/category so this
            context['categories'] = None;
            the_category = Category.objects.get(slug = category_name);
            context['image'] = "background-image : url("+the_category.image+");";
            context['color'] = "background-color : " + the_category.color;
            posters = Post.objects.filter(state = True, category = the_category)[::-1]; #this form flips the list;
            context['posters'] = posters;
        except ObjectDoesNotExist as e:
            context['error'] = e;

    return render(request, "blog/category.html", context);

#------Blog page------#(1)
def blog(request):
    context = {};
    posters = Post.objects.filter(state = True, type = 'B')[::-1]; #this form flips the list;
    context['posters'] = posters;

    return render(request, "blog/blog.html", context);

#------tutorial page------#(1)
def tutorial(request):
    context = {};
    posters = Post.objects.filter(state = True, type = 'T')[::-1]; #this form flips the list;
    context['posters'] = posters;

    return render(request, "blog/tutorial.html", context);

#------contact page------#
def contact(request):
    context = {};
    return render(request, "blog/contact.html", context);

#------post page------#
def post(request, slug):
    context = {};

    try:
        # if exist slug/category so doing this
        post = Post.objects.get(state = True, slug = slug);#this form flips the list;
        context['post'] = post;
        context['image'] = "background-image : url("+post.image+");";
        context['color'] = "background-color : " + post.color;
    except ObjectDoesNotExist as e:
        return redirect('blog:home');

    return render(request, "blog/post.html", context);
