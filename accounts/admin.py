from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'nama_lengkap', 'jabatan', 'role', 'is_active', 'date_joined')
    list_filter = ('role', 'is_active')
    search_fields = ('username', 'nama_depan', 'nama_panjang', 'jabatan')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Identitas', {'fields': ('nama_depan', 'nama_panjang', 'jabatan')}),
        ('Role & Akses', {'fields': ('role',)}),
        ('Status Akun', {'fields': ('is_active',)}),
        ('Tanggal', {'fields': ('last_login', 'date_joined'), 'classes': ('collapse',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        ('Identitas', {'fields': ('nama_depan', 'nama_panjang', 'jabatan')}),
        ('Role & Akses', {'fields': ('role',)}),
    )
