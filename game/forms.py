from django.forms import ModelForm
from .models import Member


class GameForm(ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email_address', 'phone_number', ]
