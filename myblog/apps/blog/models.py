from django.db import models
from ckeditor.fields import RichTextField;
from colorfield.fields import ColorField;


# Create your models here.
class ColorAndImage(models.Model):
    image = models.URLField('Imagen', null = True, blank = True, default = None);
    color = ColorField('color', default='#FFFFFF', null = True, blank = True);

    class Meta:
        abstract = True;

    def __str__(self):
        return self.color;


class baseModel(models.Model):
    id = models.AutoField('Index', primary_key = True);
    name = models.CharField('Nombre', max_length = 100, null = False, blank = False);
    state = models.BooleanField('Estado activo/inactivo', default = True);
    creation_date = models.DateField('Fecha creacion', auto_now = False, auto_now_add = True);

    class Meta:
        abstract = True;

    def __str__(self):
        return self.name;

class Category(baseModel, ColorAndImage):
    description = models.CharField('description', max_length = 255, null = False, blank = False);
    slug = models.CharField('slug', max_length = 100, null = False, blank = False);

    class Meta:
        verbose_name = 'Categoria';
        verbose_name_plural = 'Categorias';

class Author(baseModel):
    name = models.CharField('Nombre autor', max_length = 255, null = False, blank = False);
    last_name = models.CharField('Apellidos autor', max_length = 255, null = False, blank = False);
    facebook = models.URLField('Facebook', null = True, blank = True);
    twitter = models.URLField('twitter', null = True, blank = True);
    instagram = models.URLField('instagram', null = True, blank = True);
    email = models.EmailField("Correo Electronico", null = False, blank = False);

    def Category(baseModel):
        class Meta:
            verbose_name = 'Autor';
            verbose_name_plural = 'Autores';

    def __str__(self):
        return "{},{}".format(self.name, self.last_name);

class Post(baseModel, ColorAndImage):
    TYPE_POST = (
        ('B', 'Blog'),
        ('T', 'Tutorial'),
    )

    name = models.CharField('Titulo', max_length = 90, null = False, blank = False);
    slug = models.CharField('Slug', max_length = 100, null = False, blank = False);
    description = models.CharField('Descripcion', max_length = 110, null = False, blank = False);
    content = RichTextField('contenido');
    author = models.ForeignKey(Author, on_delete = models.CASCADE);
    category = models.ForeignKey(Category,on_delete = models.CASCADE);
    type = models.CharField('tipo', max_length = 1, null = False, blank = False, choices = TYPE_POST);

    class Meta:
        verbose_name = 'Post';
        verbose_name_plural = 'Posts';
