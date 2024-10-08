# Generated by Django 5.1.1 on 2024-09-26 09:32

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0012_suketkematian"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="SuketPenghasilanTidakTetap",
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
                ("nama", models.CharField(max_length=255)),
                ("umur", models.CharField(max_length=255)),
                ("pekerjaan", models.CharField(max_length=255)),
                ("alamat", models.CharField(max_length=255)),
                (
                    "date",
                    models.DateTimeField(blank=True, default=django.utils.timezone.now),
                ),
                ("status", models.BooleanField(blank=True, null=True)),
                ("pengantarrt", models.URLField(blank=True, null=True)),
                ("scankk", models.URLField(blank=True, null=True)),
                (
                    "penulis",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
