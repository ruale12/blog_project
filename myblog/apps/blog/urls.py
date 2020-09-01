from django.urls import path
from . import views;

urlpatterns = [
    path('', views.index, name = "home"),
    path('categorias/', views.category, name = "categorias"),
    path('blog/', views.blog, name = "blog"),
    path('tutoriales/', views.tutorial, name = "tutoriales"),
]
