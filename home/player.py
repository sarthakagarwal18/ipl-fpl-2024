from django.shortcuts import render, redirect
from . import utils, meta

def player(request):
  points = utils.create_tuples(utils.get_data('B08:O21', 'COLUMNS'))
  kohli_points = points[0]
  sahoo_points = points[1]
  sarthak_coe_points = points[2]
  boss_points = points[3]
  mittal_points = points[4]
  sandy_points = points[5]
  sarthak_it_points = points[6]
  last_update_time, matches = meta.get_meta()
  context = {
    'segment'  : 'player',
    'kohli_points'  : kohli_points,
    'sahoo_points'  : sahoo_points,
    'sarthak_coe_points'  : sarthak_coe_points,
    'boss_points'  : boss_points,
    'mittal_points'  : mittal_points,
    'sandy_points'  : sandy_points,
    'sarthak_it_points'  : sarthak_it_points,
    'matches': matches,
    'last_update_time': last_update_time
  }
  return render(request, "pages/player.html", context)