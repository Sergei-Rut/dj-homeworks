# Generated by Django 3.2.9 on 2021-12-01 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0004_auto_20211201_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
