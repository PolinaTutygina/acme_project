# Generated by Django 3.2.16 on 2024-12-12 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0005_birthday_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='birthday',
            name='author',
        ),
    ]
