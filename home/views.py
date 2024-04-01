from django.shortcuts import render, redirect
from . import utils, meta

def index(request):
  points = utils.create_dictionaries(utils.get_data('B24:O30', 'COLUMNS'))
  batting_points = points[0]
  bowling_points = points[1]
  overall_points = points[2]
  sixes_points = points[3]
  catches_points = points[4]
  max_points_points = points[5]
  max_wickets_points = points[6]
  last_update_time, matches = meta.get_meta()
  context = {
    'segment'  : 'index',
    'batting_points'  : batting_points,
    'bowling_points'  : bowling_points,
    'overall_points'  : overall_points,
    'sixes_points'  : sixes_points,
    'catches_points'  : catches_points,
    'max_points_points'  : max_points_points,
    'max_wickets_points'  : max_wickets_points,
    'matches': matches,
    'last_update_time': last_update_time
  }
  return render(request, "pages/index.html", context)