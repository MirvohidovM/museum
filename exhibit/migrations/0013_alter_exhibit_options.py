# Generated by Django 3.2.13 on 2022-06-23 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exhibit', '0012_auto_20220623_0734'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exhibit',
            options={'ordering': ('-created_at',), 'verbose_name': 'Eksponat', 'verbose_name_plural': 'Eksponatlar'},
        ),
    ]
