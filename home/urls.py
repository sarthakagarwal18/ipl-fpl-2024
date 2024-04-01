from django.urls import path
from django.contrib.auth import views as auth_views

from . import views, winnings, player

urlpatterns = [
  path(''       , views.index,  name='index'),
  path('winnings'       , winnings.winnings,  name='winnings'),
  path('player'       , player.player,  name='player'),
  path(''       , views.index,  name='subs'),
  path(''       , views.index,  name='chart'),
  path(''       , views.index,  name='teams'),
  path(''       , views.index,  name='auction'),
  path(''       , views.index,  name='rules'),
]
