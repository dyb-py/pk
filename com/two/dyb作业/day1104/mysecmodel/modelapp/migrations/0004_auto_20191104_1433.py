# Generated by Django 2.0.6 on 2019-11-04 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0003_auto_20191104_1432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='dept',
            new_name='stu',
        ),
    ]
