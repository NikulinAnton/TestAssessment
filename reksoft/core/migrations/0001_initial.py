# Generated by Django 4.1.2 on 2022-10-14 07:46

import django.db.models.deletion
from django.db import migrations, models

import core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TruckModel",
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
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        max_length=64,
                        unique=True,
                        verbose_name="Название",
                    ),
                ),
                (
                    "max_weight_capacity",
                    models.PositiveSmallIntegerField(
                        verbose_name="Максимальная грузоподъемность"
                    ),
                ),
            ],
            options={
                "verbose_name": "Модель самосвала",
                "verbose_name_plural": "Модели самосвалов",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Truck",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "deleted_at",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
                (
                    "side_number",
                    core.fields.CICharField(
                        db_index=True, max_length=10, verbose_name="Бортовой номер"
                    ),
                ),
                (
                    "current_cargo_weight",
                    models.PositiveSmallIntegerField(
                        blank=True, default=0, verbose_name="Текущий вес груза"
                    ),
                ),
                (
                    "model",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="core.truckmodel",
                        verbose_name="Модель самосвала",
                    ),
                ),
            ],
            options={
                "verbose_name": "Самосвал",
                "verbose_name_plural": "Самосвалы",
                "ordering": ["side_number"],
            },
        ),
        migrations.AddConstraint(
            model_name="truck",
            constraint=models.UniqueConstraint(
                condition=models.Q(("deleted_at__isnull", True)),
                fields=("side_number",),
                name="uniq_side_number_for_active",
            ),
        ),
    ]
