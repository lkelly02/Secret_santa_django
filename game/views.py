from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import HouseholdMemberFormSet, HouseholdFormSet
from .models import Household, HouseholdMember
import random
from os import system
# Create your views here.


def play_game(request):
    household_queryset = Household.objects.all()
    list_of_households = []
    recipients = ""
    chosen_gift_giver = []
    chosen_recipient = []
    random_recipient = ""
    for household in household_queryset:
        householdmembers = list(
            household.householdmember_set.values_list("name", flat=True))
        for member in householdmembers:
            mem = str(member)
            recipients += " ".join(mem.split(", ")) + " "

        list_of_households.append(householdmembers)

    recipients = recipients.split()

    while len(recipients) > 0:
        for household in list_of_households:
            for name in household:
                if name not in chosen_gift_giver:
                    random_recipient = random.choice(recipients)
                while name == random_recipient or random_recipient in household:
                    random_recipient = random.choice(recipients)
                    if recipients == [name, random_recipient] or recipients == [name] or (len(recipients) == 1 and recipients[0] in household):
                        recipients.extend(chosen_recipient)
                        chosen_gift_giver = []
                        chosen_recipient = []
                        system("clear")
                if name != random_recipient and random_recipient not in household:
                    chosen_gift_giver.append(name)
                    chosen_recipient.append(random_recipient)
                    recipients.remove(random_recipient)
                    print(f"{name.title()} has {random_recipient.title()}")

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
