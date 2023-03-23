# Generated by Django 3.2.14 on 2022-07-28 11:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0003_alter_event_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktiv')),
                ('title', models.CharField(max_length=256, verbose_name='Nomi')),
                ('title_uz', models.CharField(max_length=256, null=True, verbose_name='Nomi')),
                ('title_uzb', models.CharField(max_length=256, null=True, verbose_name='Nomi')),
                ('title_ru', models.CharField(max_length=256, null=True, verbose_name='Nomi')),
                ('title_en', models.CharField(max_length=256, null=True, verbose_name='Nomi')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_eventtype_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_eventtype_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tadbir turi',
                'verbose_name_plural': 'Tadbir turlari',
                'db_table': 'event_type',
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='types', to='event.eventtype'),
        ),
    ]
