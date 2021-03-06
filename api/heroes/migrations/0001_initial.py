# Generated by Django 4.0.5 on 2022-06-04 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hero",
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
                ("name", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=200)),
                ("role", models.CharField(max_length=10)),
                ("type", models.CharField(max_length=50)),
                ("description", models.TextField()),
                ("difficulty", models.CharField(max_length=10)),
                ("card_portrait", models.CharField(max_length=100)),
                ("franchise", models.CharField(max_length=20)),
                ("href", models.CharField(max_length=100)),
            ],
            options={
                "ordering": ["franchise"],
            },
        ),
    ]
