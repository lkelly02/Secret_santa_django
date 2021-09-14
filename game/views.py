from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import HouseholdMemberFormSet, HouseholdFormSet
from .models import Household, HouseholdMember
# Create your views here.


def play_game(request):
    household_queryset = Household.objects.all()
    for household in household_queryset:
        householdmembers = list(
            household.householdmember_set.values_list("name", flat=True))
        print(householdmembers)

    # households = Household.objects.values_list('name', flat=True)

    # for household in households:
    #     print(type(household))
    # print(type(households))
    # print(households)

    return render(request, 'index.html')


def householdmember_formset(request):
    householdmember_form = HouseholdMemberFormSet(
        queryset=HouseholdMember.objects.none())
    display_household_queryset = Household.objects.all()
    if request.method == 'POST':

        householdmember_form = HouseholdMemberFormSet(request.POST)

        if householdmember_form.is_valid():
            householdmember_form.save()
            # return HttpResponseRedirect('/./game/thanks')

    context = {'householdmember_form': householdmember_form,
               'Households': list(display_household_queryset)}

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
