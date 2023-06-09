# Generated by Django 3.2.13 on 2022-06-02 06:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktiv')),
                ('name', models.CharField(max_length=200, verbose_name='Nimi:')),
                ('name_uz', models.CharField(max_length=200, null=True, verbose_name='Nimi:')),
                ('name_uzb', models.CharField(max_length=200, null=True, verbose_name='Nimi:')),
                ('name_ru', models.CharField(max_length=200, null=True, verbose_name='Nimi:')),
                ('name_en', models.CharField(max_length=200, null=True, verbose_name='Nimi:')),
                ('logo', models.ImageField(upload_to='exhibit/logos/', verbose_name='Logotip: ')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exhibit_category_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exhibit_category_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
                'db_table': 'exhibit_category',
            },
        ),
        migrations.CreateModel(
            name='Exhibit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktiv')),
                ('name', models.CharField(max_length=255, verbose_name='Nomi: ')),
                ('name_uz', models.CharField(max_length=255, null=True, verbose_name='Nomi: ')),
                ('name_uzb', models.CharField(max_length=255, null=True, verbose_name='Nomi: ')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Nomi: ')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Nomi: ')),
                ('summary', models.CharField(max_length=255, verbose_name='Qisqacha: ')),
                ('summary_uz', models.CharField(max_length=255, null=True, verbose_name='Qisqacha: ')),
                ('summary_uzb', models.CharField(max_length=255, null=True, verbose_name='Qisqacha: ')),
                ('summary_ru', models.CharField(max_length=255, null=True, verbose_name='Qisqacha: ')),
                ('summary_en', models.CharField(max_length=255, null=True, verbose_name='Qisqacha: ')),
                ('used', models.CharField(max_length=100, verbose_name='Foydalanilgan vaqti: ')),
                ('used_uz', models.CharField(max_length=100, null=True, verbose_name='Foydalanilgan vaqti: ')),
                ('used_uzb', models.CharField(max_length=100, null=True, verbose_name='Foydalanilgan vaqti: ')),
                ('used_ru', models.CharField(max_length=100, null=True, verbose_name='Foydalanilgan vaqti: ')),
                ('used_en', models.CharField(max_length=100, null=True, verbose_name='Foydalanilgan vaqti: ')),
                ('invented', models.CharField(max_length=4, verbose_name='Ixtiro: ')),
                ('body', models.TextField(verbose_name='Eksponat haqida: ')),
                ('body_uz', models.TextField(null=True, verbose_name='Eksponat haqida: ')),
                ('body_uzb', models.TextField(null=True, verbose_name='Eksponat haqida: ')),
                ('body_ru', models.TextField(null=True, verbose_name='Eksponat haqida: ')),
                ('body_en', models.TextField(null=True, verbose_name='Eksponat haqida: ')),
                ('cover', models.ImageField(upload_to='exhibit/images/', verbose_name='Rasm')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to='exhibit.category', verbose_name='Kategoriya')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exhibit_exhibit_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exhibit_exhibit_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Eksponat',
                'verbose_name_plural': 'Eksponatlar',
                'db_table': 'exhibit',
            },
        ),
        migrations.CreateModel(
            name='ExhibitImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='exhibit/images/', verbose_name='Rasm: ')),
                ('exhibit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='exhibit.exhibit', verbose_name='Eksponat: ')),
            ],
            options={
                'verbose_name': 'Rasm',
                'verbose_name_plural': 'Rasmlar',
                'db_table': 'exhibit_images',
            },
        ),
    ]
