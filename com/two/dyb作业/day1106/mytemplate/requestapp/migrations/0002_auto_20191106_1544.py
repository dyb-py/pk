# Generated by Django 2.0.6 on 2019-11-06 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(),
        ),
    ]
