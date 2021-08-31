from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import HouseholdMemberForm
# Create your views here.


def play_game(request):
    return render(request, 'index.html')


def households(request):
    # # if this is a POST request we need to process the form data
    form = HouseholdMemberForm()

    if request.method == 'POST':
        #     # create a form instance and populate it with data from the request:
        form = HouseholdMemberForm(request.POST)
    #     # check whether it's valid:
        if form.is_valid():
            form.save()
    #         # process the data in form.cleaned_data as required
    #         # ...
    #         # redirect to a new URL:
    #         return HttpResponseRedirect('/./game/thanks')

    # # if a GET (or any other method) we'll create a blank form
    # else:
    #     form = HouseholdMemberForm()

    context = {'form': form}

    return render(request, 'play_by_households.html', context)


def thanks(request):
    return render(request, 'thanks.html')
