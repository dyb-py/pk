# Generated by Django 2.0.6 on 2019-11-19 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.SmallIntegerField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=7)),
                ('birthday', models.DateTimeField()),
            ],
        ),
    ]
