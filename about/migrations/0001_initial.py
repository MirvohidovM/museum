# Generated by Django 4.0.3 on 2022-05-31 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Biz haqimizda')),
                ('description_uz', models.TextField(blank=True, null=True, verbose_name='Biz haqimizda')),
                ('description_uzb', models.TextField(blank=True, null=True, verbose_name='Biz haqimizda')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Biz haqimizda')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Biz haqimizda')),
                ('on_slider', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Muzey haqida',
                'verbose_name_plural': 'Muzey haqida',
                'db_table': 'about',
            },
        ),
        migrations.CreateModel(
            name='AboutImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='AboutImages', verbose_name='Foto')),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='about.about', verbose_name='Rasmlar')),
            ],
            options={
                'db_table': 'about_images',
            },
        ),
    ]
