from django.db.models import fields
from django.forms import ModelForm
from .models import HouseholdMember


class HouseholdMemberForm(ModelForm):
    class Meta:
        model = HouseholdMember
        fields = ['name', 'email_address', 'phone_number']
