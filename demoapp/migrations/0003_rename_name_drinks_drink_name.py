# Generated by Django 4.2.1 on 2023-06-06 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_drinks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drinks',
            old_name='name',
            new_name='drink_name',
        ),
    ]