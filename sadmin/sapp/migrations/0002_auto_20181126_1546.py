# Generated by Django 2.1.3 on 2018-11-26 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, to='sapp.Student'),
        ),
    ]
