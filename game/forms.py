from django.forms import modelformset_factory, ModelForm
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


# class HouseholdMemberFormSetHelper(FormHelper):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_id = 'id-exampleForm'
#         self.helper.form_class = 'blueForms'
#         self.helper.form_method = 'post'
#         self.helper.form_action = 'submit_survey'
#         self.helper.add_input(Button('submit', 'Submit'))


HouseholdMemberFormSet = modelformset_factory(
    HouseholdMember, form=HouseholdMemberForm)


HouseholdFormSet = modelformset_factory(Household, HouseholdForm)
