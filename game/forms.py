from django.forms import modelformset_factory
from .models import HouseholdMember


HouseholdMemberFormSet = modelformset_factory(
    HouseholdMember, fields=('name', 'email_address', 'phone_number', 'household'))
