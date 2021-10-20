from django.http import HttpResponseRedirect
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from twilio.rest import Client
from .forms import HouseholdMemberFormSet, HouseholdFormSet, GroupMemberFormSet
from .models import Household, HouseholdMember, GroupMember
import os
import random


def play_game_by_households(request):
    """The main function of the secret santa game. This function will gather the households and their members
    and return the results of name drawings"""

    # variables used throughout script
    list_of_households = []
    chosen_gift_giver = []
    chosen_recipient = []
    recipients = ""
    random_recipient = ""
    results_of_game = []

    # variables related to sending the sms to each player
    from_ = os.environ['TWILIO_PHONE_NUMBER']
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']

    # to instantiate the twilio API
    client = Client(account_sid, auth_token)

    # Get the list of current households in the database
    household_queryset = Household.objects.all()

    # For each household in the database, get the household members associated to it, and add them to a list.
    for household in household_queryset:
        householdmembers = list(
            household.householdmember_set.values_list('name', flat=True))

        # Extract the household members from each household, and add them to a string of all household members in the game
        for name in householdmembers:
            recipients += " ".join(name.split(", ")) + " "
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
                giver = HouseholdMember.objects.get(name=name)

                # Check to see if the current household member has already chosen their recipient.
                # If not, choose a recipient from the recipient list.
                if name not in chosen_gift_giver:
                    random_recipient = random.choice(recipients)
                # If current household member has already chosen their recipient, skip to next member, or next household.
                else:
                    break
                # If the current household member, picks their name, or the name of someone in THEIR household, another recpient is chosen.
                while name == random_recipient or random_recipient in household:
                    random_recipient = random.choice(recipients)
                    # In the event that the remaining household member can only pick either their name, or someone in their household,
                    # The game will automatically clear the chosen gift giver list and chosen recipient list. Game will continue on the current household member.
                    if recipients == [name, random_recipient] or recipients == [name]:
                        recipients.extend(chosen_recipient)
                        chosen_gift_giver = []
                        chosen_recipient = []
                        results_of_game = []
                        break
                    elif (len(recipients) == len(household) and recipients == household):
                        return HttpResponseRedirect('/./game/error')

                # As long as the current household member does not pick their name, or someone from their hosuehold,
                # their name will be added to the chosen gift giver list as already picking a name.
                # The name that was picked, will be added to the chosen recipients list, and removed from the initial recipients list.
                if name != random_recipient and random_recipient not in household:
                    chosen_gift_giver.append(name)
                    chosen_recipient.append(random_recipient)
                    recipients.remove(random_recipient)
                    results_of_game.append(
                        f"{name.title()} has {random_recipient.title()}")
                    get_givers_number = giver.phone_number
                    giver.recipient = random_recipient
                    giver.save()
                    if get_givers_number == '':
                        pass
                    print(f"{name.title()} has {random_recipient.title()}")
                    # message = client.messages.create(
                    #     body=f"The person you have for secret santa is...{random_recipient.title()}",
                    #     from_=from_,
                    #     to=str(get_givers_number)
                    # )
                    # message.feedback

    return render(request, 'index.html', context={'results': results_of_game})


def play_game_by_groups(request):
    # variables used throughout script
    chosen_gift_giver = []
    chosen_recipient = []
    random_recipient = ""
    results_of_game = []

    members = list(
        GroupMember.objects.values_list('name', flat=True))

    recipients = list(
        GroupMember.objects.values_list('name', flat=True))

    while len(recipients) > 0:
        for name in members:
            if name not in chosen_gift_giver:
                random_recipient = random.choice(recipients)
            else:
                break
            while name == random_recipient:
                random_recipient = random.choice(recipients)
                if recipients == [name]:
                    recipients.extend(chosen_recipient)
                    chosen_gift_giver = []
                    chosen_recipient = []
            if name != random_recipient:
                chosen_gift_giver.append(name)
                chosen_recipient.append(random_recipient)
                recipients.remove(random_recipient)
                print(f"{name.title()} has {random_recipient.title()}")

    context = {'members': list(members)}
    return render(request, 'play_by_groups.html', context)


def add_householdmember(request):
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
            return HttpResponseRedirect('/./game/play_by_households/add_householdmember')

    context = {'householdmember_form': householdmember_form,
               'Households': list(display_household_queryset), 'householdmembers': members_list}

    return render(request, 'play_by_households.html', context)


def add_household_formset(request):
    form = HouseholdFormSet(queryset=Household.objects.none())

    if request.method == 'POST':

        form = HouseholdFormSet(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/./game/play_by_households/add_householdmember')
    context = {'householdform': form}

    return render(request, 'add_household.html', context)


def add_group_members(request):
    """To add members to one group, rather than households."""
    groupmember_form = GroupMemberFormSet(queryset=GroupMember.objects.none())

    if request.method == 'POST':
        groupmember_form = GroupMemberFormSet(request.POST)

        if groupmember_form.is_valid():
            groupmember_form.save()
            return HttpResponseRedirect('/./game/play_by_groups/add_group_members')

    queryset = GroupMember.objects.all()
    context = {'groupmember_form': groupmember_form, 'members': list(queryset)}
    return render(request, 'add_groupmembers.html', context)


def thanks(request):
    return render(request, 'thanks.html')


def error_page(request):
    return render(request, 'error_page.html')
