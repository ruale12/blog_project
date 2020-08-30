from django.shortcuts import render
from .models import Category;
# Create your views here.

def index(request):
    return render(request, "blog/index.html");

def category(request):
    context = {};
    categories = Category.objects.all();
    context['categories'] = categories;

    return render(request, "blog/category.html", context);
