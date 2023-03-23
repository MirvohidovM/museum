# Generated by Django 4.0.3 on 2022-06-01 09:13

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
            name='Employee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktiv')),
                ('name', models.CharField(max_length=500, verbose_name="To'liq Ism")),
                ('name_uz', models.CharField(max_length=500, null=True, verbose_name="To'liq Ism")),
                ('name_uzb', models.CharField(max_length=500, null=True, verbose_name="To'liq Ism")),
                ('name_ru', models.CharField(max_length=500, null=True, verbose_name="To'liq Ism")),
                ('name_en', models.CharField(max_length=500, null=True, verbose_name="To'liq Ism")),
                ('position', models.CharField(max_length=500, verbose_name='Lavozim')),
                ('position_uz', models.CharField(max_length=500, null=True, verbose_name='Lavozim')),
                ('position_uzb', models.CharField(max_length=500, null=True, verbose_name='Lavozim')),
                ('position_ru', models.CharField(max_length=500, null=True, verbose_name='Lavozim')),
                ('position_en', models.CharField(max_length=500, null=True, verbose_name='Lavozim')),
                ('phone', models.CharField(max_length=13, verbose_name='Telefon raqam')),
                ('email', models.EmailField(max_length=254, verbose_name='Elektron pochta')),
                ('photo', models.ImageField(upload_to='EmployeeImages', verbose_name='Rasm')),
                ('is_lidership', models.BooleanField(default=False, verbose_name='Rahbariyat')),
                ('index', models.IntegerField(blank=True, null=True, verbose_name='Tartib raqami')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Hodim',
                'verbose_name_plural': 'Hodimlar',
                'db_table': 'employee',
                'ordering': ['-index'],
            },
        ),
    ]
