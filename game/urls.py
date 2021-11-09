from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('play_by_households/', views.play_game_by_households),
    path('play_by_households/add_householdmembers/', views.add_householdmember),
    path('play_by_groups/', views.play_game_by_groups),
    path('play_by_groups/add_group_members', views.add_group_members),
    path('thanks/', views.thanks),
    path('error/', views.error_page),
    path('test/', views.PlayByHouseholds.as_view())
]
