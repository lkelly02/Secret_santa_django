from django.contrib import admin
from . import models
from django.urls import reverse
from django.utils.html import format_html, urlencode
from django.db.models.aggregates import Count

# Register your models here.


@admin.register(models.HouseholdMember)
class HouseholdMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'email_address',
                    'phone_number', 'household', 'recipient']
    list_select_related = ['household']


@admin.register(models.Household)
class HouseholdAdmin(admin.ModelAdmin):
    list_display = ['name', 'members']

    def members(self, household):
        url = (
            reverse('admin:game_householdmember_changelist')
            + '?'
            + urlencode({
                'household__id': str(household.id)
            })

        )

        return format_html('<a href="{}">{}</a>', url, household.members)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            members=Count('householdmember')
        )


@ admin.register(models.GroupMember)
class GroupMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'email_address', 'phone_number']
