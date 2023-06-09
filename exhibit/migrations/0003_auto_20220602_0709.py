# Generated by Django 3.2.13 on 2022-06-02 07:09

import config.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibit', '0002_auto_20220602_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibit',
            name='audio',
            field=models.FileField(blank=True, upload_to='exhibit/audios/', validators=[config.utils.validate_file_extension], verbose_name='Audio: '),
        ),
        migrations.AlterField(
            model_name='exhibit',
            name='audio_en',
            field=models.FileField(blank=True, null=True, upload_to='exhibit/audios/', validators=[config.utils.validate_file_extension], verbose_name='Audio: '),
        ),
        migrations.AlterField(
            model_name='exhibit',
            name='audio_ru',
            field=models.FileField(blank=True, null=True, upload_to='exhibit/audios/', validators=[config.utils.validate_file_extension], verbose_name='Audio: '),
        ),
        migrations.AlterField(
            model_name='exhibit',
            name='audio_uz',
            field=models.FileField(blank=True, null=True, upload_to='exhibit/audios/', validators=[config.utils.validate_file_extension], verbose_name='Audio: '),
        ),
        migrations.AlterField(
            model_name='exhibit',
            name='audio_uzb',
            field=models.FileField(blank=True, null=True, upload_to='exhibit/audios/', validators=[config.utils.validate_file_extension], verbose_name='Audio: '),
        ),
    ]
