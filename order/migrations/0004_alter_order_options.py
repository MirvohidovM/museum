# Generated by Django 3.2.13 on 2022-06-17 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_excursiontype_table_alter_order_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['visit_time'], 'verbose_name': 'Onlayn buyurtma', 'verbose_name_plural': 'Onlayn buyurtmalar'},
        ),
    ]