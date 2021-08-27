from django.forms import ModelForm
from .models import HouseholdMember


class GameForm(ModelForm):
    class Meta:
        model = HouseholdMember
        fields = ['name', 'email_address', 'phone_number', ]
