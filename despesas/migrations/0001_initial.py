# Generated by Django 4.2.5 on 2023-09-04 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("caixas", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Despesa",
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
                ("nome", models.CharField(max_length=250)),
                ("valor", models.DecimalField(decimal_places=2, max_digits=7)),
                (
                    "caixa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="despesas",
                        to="caixas.caixa",
                    ),
                ),
            ],
        ),
    ]