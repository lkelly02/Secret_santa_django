from django.urls import path
from . import views


urlpatterns = [
    path('', views.play_game),
    path('play_by_households/', views.households_formset),
    path('thanks/', views.thanks)
]
