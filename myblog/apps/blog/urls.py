from django.urls import path
from . import views;

urlpatterns = [
    path('', views.index, name = "home"),
    path('categorias/', views.category, name = "categorias"),
    path('categorias/<category_name>', views.category, name = "categoria_name"),
    path('blog/', views.blog, name = "blog"),
    path('tutoriales/', views.tutorial, name = "tutoriales"),
    path('contacto/', views.contact, name = "contacto"),
]
