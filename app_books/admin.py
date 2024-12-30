from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import AccountUser


class CustomUserAdmin(UserAdmin):
    model = AccountUser
    fieldsets = UserAdmin.fieldsets


admin.site.register(AccountUser, CustomUserAdmin)
