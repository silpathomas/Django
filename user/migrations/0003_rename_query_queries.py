# Generated by Django 3.2 on 2022-06-03 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_query'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Query',
            new_name='Queries',
        ),
    ]
