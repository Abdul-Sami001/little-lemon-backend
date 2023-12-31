# Generated by Django 4.2.1 on 2023-06-06 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("demoapp", "0003_rename_name_drinks_drink_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Drink_Categories",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("drink_category", models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name="drinks",
            name="drink_category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="demoapp.drink_categories",
            ),
            preserve_default=False,
        ),
    ]
