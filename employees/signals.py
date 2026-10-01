from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import EmployeeProfile


@receiver(post_save, sender=User)
def create_employee_profile(sender, instance, created, **kwargs):
    """Автоматически создает профиль при создании нового пользователя"""
    if created:
        EmployeeProfile.objects.create(
            user=instance,
            first_name=instance.first_name or instance.username,
            last_name=instance.last_name or ""
        )


@receiver(post_save, sender=User)
def save_employee_profile(sender, instance, **kwargs):
    """Автоматически сохраняет профиль при обновлении пользователя"""
    if hasattr(instance, 'profile'):
        instance.profile.save()
