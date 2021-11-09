from django.forms import modelformset_factory, ModelForm, BooleanField
from django.forms.widgets import HiddenInput
from .models import HouseholdMember, Household, GroupMember


class HouseholdForm(ModelForm):
    """The form to create an instance of the Household model."""
    add_household = BooleanField(widget=HiddenInput, initial=True)

    class Meta:
        model = Household
        fields = ("name",)


class HouseholdMemberForm(ModelForm):
    """The form to create an instance of a household member."""

    add_householdmember = BooleanField(widget=HiddenInput, initial=True)

    class Meta:
        model = HouseholdMember
        fields = ("name", "email_address", "phone_number", "household")


# The use of a Formset, so multiple instances of the form can be applied to one HTML template.
HouseholdMemberFormSet = modelformset_factory(
    HouseholdMember, form=HouseholdMemberForm)


HouseholdFormSet = modelformset_factory(Household, form=HouseholdForm, extra=4)


class GroupMemberForm(ModelForm):
    """The form to create an instance of a group member."""
    class Meta:
        model = GroupMember
        fields = ("name", "phone_number", "email_address")


GroupMemberFormSet = modelformset_factory(
    GroupMember, form=GroupMemberForm)
