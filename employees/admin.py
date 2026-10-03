from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import EmployeeProfile, EmployeeImage, Skill, EmployeeSkill


# 1. Объявляем инлайн для картинок
class EmployeeImageInline(admin.TabularInline):
    model = EmployeeImage
    extra = 1
    fields = ['image', 'position']
    ordering = ['position']


# 2. Объявляем инлайн для навыков
class EmployeeSkillInline(admin.TabularInline):
    model = EmployeeSkill
    extra = 1


# 3. Регистрируем навык (только ОДИН раз)
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)


# 4. Регистрируем профиль сотрудника и подключаем ОБА инлайна внутрь класса
@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'gender')
    # Теперь здесь находятся оба инлайна:
    inlines = [EmployeeSkillInline, EmployeeImageInline]


# Переименование встроенных моделей в админке
Group._meta.verbose_name = 'Группа'
Group._meta.verbose_name_plural = 'Группы'
User._meta.verbose_name = 'Пользователь'
User._meta.verbose_name_plural = 'Пользователи'
