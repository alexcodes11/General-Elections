# Generated by Django 4.1.2 on 2022-10-17 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0004_alter_transportation_quotes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transportation',
            name='quotes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transportation',
            name='website_found',
            field=models.TextField(blank=True, null=True),
        ),
    ]
