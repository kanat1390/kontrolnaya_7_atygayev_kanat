# Generated by Django 4.1.1 on 2022-10-01 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='name',
            new_name='author',
        ),
    ]
