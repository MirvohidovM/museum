# Generated by Django 3.2.13 on 2022-06-29 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(upload_to='news', verbose_name='Asosiy rasm'),
        ),
    ]
