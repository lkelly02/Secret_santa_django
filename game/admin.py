from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.HouseholdMember)
class HouseholdMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'email_address', 'phone_number', 'household']


@admin.register(models.Household)
class HouseholdAdmin(admin.ModelAdmin):
    list_display = ['name', 'members']

    def members(self, members):
        pass


@admin.register(models.GroupMember)
class GroupMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'email_address', 'phone_number']
