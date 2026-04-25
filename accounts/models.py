from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    SCORING = 'scoring'
    MANAGER = 'manager'
    SUPERVISOR = 'supervisor'
    ADMIN = 'admin'
    SUPERADMIN = 'superadmin'

    ROLE_CHOICES = [
        (SCORING, 'Scoring'),
        (MANAGER, 'Manager'),
        (SUPERVISOR, 'Supervisor'),
        (ADMIN, 'Admin'),
        (SUPERADMIN, 'Superadmin'),
    ]

    ROLE_LEVEL = {
        SCORING: 1,
        MANAGER: 2,
        SUPERVISOR: 3,
        ADMIN: 4,
        SUPERADMIN: 5,
    }

    # Identitas
    nama_depan = models.CharField(max_length=50, blank=True, verbose_name='Nama Depan')
    nama_panjang = models.CharField(max_length=100, blank=True, verbose_name='Nama Panjang')
    jabatan = models.CharField(max_length=100, blank=True, verbose_name='Jabatan')

    # Akses sistem
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=SCORING, verbose_name='Role')

    # Sembunyikan first_name / last_name bawaan AbstractUser
    first_name = None
    last_name = None

    @property
    def nama_lengkap(self):
        if self.nama_depan and self.nama_panjang:
            return f"{self.nama_depan} {self.nama_panjang}"
        return self.nama_depan or self.nama_panjang or self.username

    def save(self, *args, **kwargs):
        if self.role == self.SUPERADMIN:
            self.is_staff = True
            self.is_superuser = True
        else:
            self.is_staff = False
            self.is_superuser = False
        super().save(*args, **kwargs)

    @property
    def role_level(self):
        return self.ROLE_LEVEL.get(self.role, 0)

    def has_role(self, *roles):
        return self.role in roles

    def has_min_role(self, min_role):
        return self.role_level >= self.ROLE_LEVEL.get(min_role, 0)

    def __str__(self):
        return f"{self.nama_lengkap} ({self.get_role_display()})"
