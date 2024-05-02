from django.contrib import admin
from .models import (
    Client,
    Coach,
    Equipment,
    Pass,
    Training
)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id_client', 'first_name', 'last_name', 'patronymic', 'dob', 'phone', 'having_pass', 'having_coach')


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('id_coach', 'first_name', 'last_name', 'patronymic', 'dob', 'qualification')


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('id_equipment', 'id_client', 'appellation', 'purpose')


@admin.register(Pass)
class PassAdmin(admin.ModelAdmin):
    list_display = ('id_pass', 'id_client', 'type', 'expiration_date')


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ('id_training', 'id_client', 'id_coach', 'date', 'duration')


