from django.urls import path
from . import views


urlpatterns = [
    path('', views.play_game),
    path('play_by_households/', views.add_householdmember),
    path('play_by_households/add_household/', views.add_household_formset),
    path('thanks/', views.thanks)
]
