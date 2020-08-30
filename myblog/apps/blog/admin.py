from django.contrib import admin
from .models import Category, Author, Post;
from import_export import resources
from import_export.admin import ImportExportModelAdmin



# Classes here
class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category;

class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author;
        
class PostResource(resources.ModelResource):
    class Meta:
        model = Post;

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name'];
    list_display = ('name','state',)
    resource_class = CategoryResource;

class AuthorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name','last_name','email'];
    list_display = ('name','last_name','email','state', 'creation_date');
    resource_class = AuthorResource;

class PostAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name','slug','description','content','image','author','Category'];
    list_display = ('name','slug','description','content','image','author','Category',);
    resource_class = PostResource;

# Register your models here.
admin.site.register(Category, CategoryAdmin);
admin.site.register(Author, AuthorAdmin);
admin.site.register(Post, PostAdmin);
