# Generated by Django 3.0.9 on 2020-08-06 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_auto_20200805_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]