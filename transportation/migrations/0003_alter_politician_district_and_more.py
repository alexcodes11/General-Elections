# Generated by Django 4.1.2 on 2022-10-16 09:19

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0002_alter_transportation_quotes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='politician',
            name='district',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='transportation',
            name='website_found',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, null=True, size=None),
        ),
    ]
