# Generated by Django 3.1 on 2020-09-02 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200830_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(default=1, max_length=100, verbose_name='Slug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('B', 'Blog'), ('T', 'Tutorial')], max_length=1, verbose_name='tipo'),
        ),
    ]
