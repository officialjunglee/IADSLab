# Generated by Django 4.2.6 on 2023-11-05 00:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myappF23", "0005_order"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("email", models.CharField(max_length=50)),
                ("age", models.IntegerField()),
                ("gender", models.CharField(max_length=90)),
                ("contact_no", models.CharField(max_length=10)),
                ("country", models.CharField(max_length=100)),
            ],
        ),
    ]
