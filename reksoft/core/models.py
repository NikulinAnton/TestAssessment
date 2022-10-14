from django.db import models
from django.db.models import Q
from django_paranoid.models import ParanoidModel

from core.fields import CICharField


class TruckModel(models.Model):
    name = models.CharField(
        max_length=64, verbose_name="Название", unique=True, db_index=True
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Модель самосвала"
        verbose_name_plural = "Модели самосвалов"

    def __str__(self):
        return f"{self.name}"


class Truck(ParanoidModel):
    side_number = CICharField(
        max_length=10, verbose_name="Бортовой номер", db_index=True
    )
    model = models.ForeignKey(
        TruckModel, on_delete=models.PROTECT, verbose_name="Модель самосвала"
    )
    max_weight_capacity = models.PositiveSmallIntegerField(
        verbose_name="Максимальная грузоподъемность"
    )
    current_cargo_weight = models.PositiveSmallIntegerField(
        verbose_name="Текущий вес груза", blank=True, default=0
    )

    class Meta:
        ordering = ["side_number"]
        verbose_name = "Самосвал"
        verbose_name_plural = "Самосвалы"
        constraints = [
            models.UniqueConstraint(
                fields=["side_number"],
                condition=Q(deleted_at__isnull=True),
                name="uniq_side_number_for_active",
            )
        ]

    def __str__(self):
        return f"{self.side_number}"
