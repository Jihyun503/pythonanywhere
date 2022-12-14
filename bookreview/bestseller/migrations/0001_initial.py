# Generated by Django 4.1 on 2022-08-26 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bestseller",
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
                ("rank", models.IntegerField()),
                ("title", models.CharField(max_length=64)),
                ("author", models.CharField(max_length=32)),
                ("price", models.IntegerField()),
                ("pub_date", models.CharField(max_length=10)),
                ("bookcover", models.TextField()),
                ("standard_week", models.CharField(max_length=6)),
            ],
        ),
    ]
