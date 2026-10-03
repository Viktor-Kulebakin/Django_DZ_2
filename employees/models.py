from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название навыка")

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return self.name


class EmployeeProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name="Пользователь"
    )
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    middle_name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Отчество"
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        verbose_name="Пол"
    )
    skills = models.ManyToManyField(
        'Skill',
        through='EmployeeSkill',
        verbose_name="Навыки"
    )
    description = RichTextField(
        blank=True,
        null=True,
        verbose_name="Описание"
    )

    class Meta:
        verbose_name = "Профиль сотрудника"
        verbose_name_plural = "Профили сотрудников"

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class EmployeeSkill(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name="Уровень освоения (1-10)"
    )

    class Meta:
        verbose_name = "Навык сотрудника"
        verbose_name_plural = "Навыки сотрудников"
        unique_together = ('employee', 'skill')

    def __str__(self):
        return f"{self.skill.name} ({self.level})"

    
class EmployeeImage(models.Model):
    employee = models.ForeignKey(
        EmployeeProfile, 
        on_delete=models.CASCADE, 
        related_name='images', 
        verbose_name="Сотрудник"
    )
    
    # Заменили на FileField. Загрузка в папку media/employee_gallery/
    image = models.FileField(
        upload_to='employee_gallery/', 
        verbose_name="Файл изображения"
    )
    
    position = models.PositiveIntegerField(
        default=1, 
        verbose_name="Порядковый номер"
    )

    class Meta:
        verbose_name = "Изображение сотрудника"
        verbose_name_plural = "Галерея изображений"
        ordering = ['position', 'id']

    def __str__(self):
        return f"Фото {self.position} для {self.employee.last_name}"