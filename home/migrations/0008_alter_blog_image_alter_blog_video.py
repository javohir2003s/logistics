# Generated by Django 4.2.10 on 2024-03-02 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_blog_source_blog_image_blog_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blogs', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='blogs', verbose_name='Video'),
        ),
    ]
