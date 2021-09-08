from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import HouseholdMemberFormSet, HouseholdFormSet
from .models import Household, HouseholdMember
# Create your views here.


def play_game(request):
    return render(request, 'index.html')


def householdmember_formset(request):
    form = HouseholdMemberFormSet(queryset=HouseholdMember.objects.none())
    household_queryset = Household.objects.all()
    # helper = HouseholdMemberFormSetHelper()
    if request.method == 'POST':

        form = HouseholdMemberFormSet(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/./game/thanks')
    context = {'forms': form, 'Households': list(
        household_queryset)}

    # add in 'helper': helper, to context if you uncomment helper variable.

    return render(request, 'play_by_households.html', context)


def add_household_formset(request):
    form = HouseholdFormSet(queryset=Household.objects.none())

    if request.method == 'POST':

        form = HouseholdFormSet(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/./game/play_by_households')
    context = {'householdform': form}

    return render(request, 'add_household.html', context)


def remove_household_formset(request):
    household_list = Household.objects.all()

    context = {'Household_list': list(household_list)}

    return render(request, 'remove_household.html', context)


def thanks(request):
    return render(request, 'thanks.html')
