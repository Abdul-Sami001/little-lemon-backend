# Generated by Django 4.2.1 on 2023-06-17 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0004_drink_categories_drinks_drink_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_log', models.TimeField()),
            ],
        ),
    ]