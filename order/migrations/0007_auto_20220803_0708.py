# Generated by Django 3.2.14 on 2022-08-03 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20220629_1102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='excursiontype',
            options={'verbose_name': 'Экскурсия тури', 'verbose_name_plural': 'Экскурсия турлари'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['visit_time'], 'verbose_name': 'Онлайн буюртма', 'verbose_name_plural': 'Онлайн буюртмалар'},
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Электрон почтаси'),
        ),
        migrations.AlterField(
            model_name='order',
            name='excursion_lan',
            field=models.CharField(choices=[['uz', "O'zbekcha"], ['ru', 'Ruscha'], ['en', 'Inglizcha']], max_length=254, verbose_name='Экскурсия тили'),
        ),
        migrations.AlterField(
            model_name='order',
            name='excursion_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.excursiontype', verbose_name='Экскурсия тури'),
        ),
        migrations.AlterField(
            model_name='order',
            name='firstname',
            field=models.CharField(max_length=254, verbose_name='Исм'),
        ),
        migrations.AlterField(
            model_name='order',
            name='firstname_en',
            field=models.CharField(max_length=254, null=True, verbose_name='Исм'),
        ),
        migrations.AlterField(
            model_name='order',
            name='firstname_ru',
            field=models.CharField(max_length=254, null=True, verbose_name='Исм'),
        ),
        migrations.AlterField(
            model_name='order',
            name='firstname_uz',
            field=models.CharField(max_length=254, null=True, verbose_name='Исм'),
        ),
        migrations.AlterField(
            model_name='order',
            name='firstname_uzb',
            field=models.CharField(max_length=254, null=True, verbose_name='Исм'),
        ),
        migrations.AlterField(
            model_name='order',
            name='lastname',
            field=models.CharField(max_length=254, verbose_name='Фамилияси'),
        ),
        migrations.AlterField(
            model_name='order',
            name='lastname_en',
            field=models.CharField(max_length=254, null=True, verbose_name='Фамилияси'),
        ),
        migrations.AlterField(
            model_name='order',
            name='lastname_ru',
            field=models.CharField(max_length=254, null=True, verbose_name='Фамилияси'),
        ),
        migrations.AlterField(
            model_name='order',
            name='lastname_uz',
            field=models.CharField(max_length=254, null=True, verbose_name='Фамилияси'),
        ),
        migrations.AlterField(
            model_name='order',
            name='lastname_uzb',
            field=models.CharField(max_length=254, null=True, verbose_name='Фамилияси'),
        ),
        migrations.AlterField(
            model_name='order',
            name='num_visitors',
            field=models.IntegerField(default=0, verbose_name='Ташрифчилар сони'),
        ),
        migrations.AlterField(
            model_name='order',
            name='organization',
            field=models.CharField(max_length=500, verbose_name='Муассаса номи'),
        ),
        migrations.AlterField(
            model_name='order',
            name='organization_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Муассаса номи'),
        ),
        migrations.AlterField(
            model_name='order',
            name='organization_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='Муассаса номи'),
        ),
        migrations.AlterField(
            model_name='order',
            name='organization_uz',
            field=models.CharField(max_length=500, null=True, verbose_name='Муассаса номи'),
        ),
        migrations.AlterField(
            model_name='order',
            name='organization_uzb',
            field=models.CharField(max_length=500, null=True, verbose_name='Муассаса номи'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=30, verbose_name='Боғланиш телефони'),
        ),
        migrations.AlterField(
            model_name='order',
            name='reason',
            field=models.TextField(blank=True, null=True, verbose_name='Рад этиш сабаби'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Янги'), (2, 'Қабул қилинди'), (3, 'Рад этилди')], default=1, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='order',
            name='visit_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Ташриф куни ва соати'),
        ),
    ]