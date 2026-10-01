from django.db import models

from employees.models import EmployeeProfile


class Workplace(models.Model):
    """Модель рабочего места"""

    table_number = models.CharField(
        max_length=10,
        unique=True,
        verbose_name="Номер стола"
    )
    additional_info = models.TextField(
        blank=True,
        null=True,
        verbose_name="Дополнительная информация"
    )
    employee = models.OneToOneField(
        EmployeeProfile,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='workplace',
        verbose_name="Сотрудник"
    )

    class Meta:
        verbose_name = "Рабочее место"
        verbose_name_plural = "Рабочие места"

    def __str__(self):
        return f"Стол №{self.table_number}"
