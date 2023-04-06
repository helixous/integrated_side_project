from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import AdministrationUser


# Register your models here.

@admin.register(AdministrationUser)
class AdministrationUserAdmin(UserAdmin):
    pass
