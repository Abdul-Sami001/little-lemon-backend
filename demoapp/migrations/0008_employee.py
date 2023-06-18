# Generated by Django 4.2.1 on 2023-06-18 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0007_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=100)),
                ('shift', models.IntegerField()),
            ],
        ),
    ]
