# Generated by Django 3.2.13 on 2022-06-22 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exhibit', '0010_remove_exhibit_evolution_remove_exhibit_is_main_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('index',), 'verbose_name': 'Kategoriya', 'verbose_name_plural': 'Kategoriyalar'},
        ),
    ]
