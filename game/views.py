from django.shortcuts import render
# Create your views here.


def play_game(request):
    return render(request, 'index.html')


def households(request):
    return render(request, 'households.html')
