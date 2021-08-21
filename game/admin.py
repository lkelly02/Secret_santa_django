from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'email_address', 'phone_number', 'household']


@admin.register(models.Household)
class HouseholdAdmin(admin.ModelAdmin):
    list_display = ['name', 'members']

    def members(self, members):
        pass
