from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import HouseholdMemberFormSet
from .models import HouseholdMember
# Create your views here.


def play_game(request):
    return render(request, 'index.html')


def households_formset(request):
    form = HouseholdMemberFormSet(queryset=HouseholdMember.objects.none())

    if request.method == 'POST':

        form = HouseholdMemberFormSet(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/./game/thanks')
    context = {'forms': form}

    return render(request, 'play_by_households.html', context)


def thanks(request):
    return render(request, 'thanks.html')
