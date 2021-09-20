from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import HouseholdMemberFormSet, HouseholdFormSet
from .models import Household, HouseholdMember
import random
from os import system
# Create your views here.


def play_game(request):
    """The main function of the secret santa game. This function will gather the households and their members
    and return the results of name drawings"""
    # Get the list of current households in the database
    household_queryset = Household.objects.all()

    list_of_households = []
    chosen_gift_giver = []
    chosen_recipient = []
    recipients = ""
    random_recipient = ""
    results_of_game = []

    # For each household in the database, get the household members associated to it, and add them to a list.
    for household in household_queryset:
        householdmembers = list(
            household.householdmember_set.values_list("name", flat=True))
        # Extract the household members from each household, and add them to a string of all household members in the game
        for member in householdmembers:
            mem = str(member)
            recipients += " ".join(mem.split(", ")) + " "
        # Creates a list containing each household member list.
        list_of_households.append(householdmembers)
    # Converts the string of all player of the game, into one list to be used in the conditional statements below.
    recipients = recipients.split()

    # As long as the list of recipients has at least one recipient, the loop continues.
    while len(recipients) > 0:
        # Starting with the first household member in the first household, loop through the below code until
        # all recipients have been chosen.
        for household in list_of_households:
            for name in household:
                # Check to see if the current household member has already chosen their recipient.
                # If not, choose a recipient from the recipient list.
                if name not in chosen_gift_giver:
                    random_recipient = random.choice(recipients)
                # If the current household member, picks their name, or the name of someone in THEIR household, another recpient is chosen.

                while name == random_recipient or random_recipient in household:
                    random_recipient = random.choice(recipients)
                    # In the event that the remaining household member can only pick either their name, or someone in their household,
                    # The game will automatically clear the chosen gift giver list and chosen recipient list. Game will continue on the current household member.
                    if recipients == [name, random_recipient] or recipients == [name] or (len(recipients) == 1 and recipients[0] in household):
                        recipients.extend(chosen_recipient)
                        chosen_gift_giver = []
                        chosen_recipient = []
                        system("clear")
                # As long as the current household member does not pick their name, or someone from their hosuehold,
                # their name will be added to the chosen gift giver list as already picking a name.
                # The name that was picked, will be added to the chosen recipients list, and removed from the initial recipients list.
                if name != random_recipient and random_recipient not in household:
                    chosen_gift_giver.append(name)
                    chosen_recipient.append(random_recipient)
                    recipients.remove(random_recipient)
                    results_of_game.append(
                        f"{name.title()} has {random_recipient.title()}")

    return render(request, 'index.html', context={'results': results_of_game})


def householdmember_formset(request):
    """The form to add a new household member object"""
    # Default the form to be empty, and hide any existing household member objects.
    householdmember_form = HouseholdMemberFormSet(
        queryset=HouseholdMember.objects.none())

    # Get the current household objects
    display_household_queryset = Household.objects.all()

    members_list = []

    for household in display_household_queryset:
        # Use the foreignkey manager to get the values for each household member associated to each household.
        get_members = household.householdmember_set.values()

        # Add each household member instance to a list of all instances
        for member in get_members:
            members_list.append(member)

    if request.method == 'POST':
        householdmember_form = HouseholdMemberFormSet(request.POST)

        if householdmember_form.is_valid():
            householdmember_form.save()
            return HttpResponseRedirect('/./game/play_by_households')

    context = {'householdmember_form': householdmember_form,
               'Households': list(display_household_queryset), 'householdmembers': members_list}

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
