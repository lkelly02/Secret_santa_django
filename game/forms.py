from django.db.models.query import QuerySet
from django.forms import modelformset_factory, ModelForm
from django.forms.models import inlineformset_factory
from .models import HouseholdMember, Household
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button


class HouseholdForm(ModelForm):
    class Meta:
        Household
        fields = ("name",)


class HouseholdMemberForm(ModelForm):
    class Meta:
        HouseholdMember
        fields = ("name", "email_address", "phone_number", "household")


HouseholdMemberFormSet = modelformset_factory(
    HouseholdMember, form=HouseholdMemberForm)


HouseholdFormSet = modelformset_factory(Household, form=HouseholdForm)
