# Generated by Django 3.2.14 on 2022-08-03 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photogallery',
            options={'ordering': ['title'], 'verbose_name': 'Фото галерея', 'verbose_name_plural': 'Фото галерея'},
        ),
        migrations.AlterField(
            model_name='photogallery',
            name='photo',
            field=models.ImageField(upload_to='images', verbose_name='Асосий расм'),
        ),
        migrations.AlterField(
            model_name='photogallery',
            name='title',
            field=models.CharField(max_length=500, verbose_name='Галерея номи'),
        ),
        migrations.AlterField(
            model_name='photogallery',
            name='title_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Галерея номи'),
        ),
        migrations.AlterField(
            model_name='photogallery',
            name='title_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='Галерея номи'),
        ),
        migrations.AlterField(
            model_name='photogallery',
            name='title_uz',
            field=models.CharField(max_length=500, null=True, verbose_name='Галерея номи'),
        ),
        migrations.AlterField(
            model_name='photogallery',
            name='title_uzb',
            field=models.CharField(max_length=500, null=True, verbose_name='Галерея номи'),
        ),
        migrations.AlterField(
            model_name='photogalleryimages',
            name='gallery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='gallery.photogallery', verbose_name='Тасвирлар'),
        ),
        migrations.AlterField(
            model_name='photogalleryimages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='PhotoGallery/', verbose_name='Расм'),
        ),
    ]
