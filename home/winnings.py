from django.shortcuts import render, redirect
from . import utils, meta

def winnings(request):
  final_winnings = utils.get_data('H43:I49', 'ROWS')
  category_winnings = utils.create_dictionaries(utils.get_data('B34:O40', 'COLUMNS'))
  batting_winnings = category_winnings[0]
  bowling_winnings = category_winnings[1]
  overall_winnings = category_winnings[2]
  sixes_winnings = category_winnings[3]
  catches_winnings = category_winnings[4]
  max_points_winnings = category_winnings[5]
  max_wickets_winnings = category_winnings[6]
  last_update_time, matches = meta.get_meta()
  context = {
    'segment'  : 'winnings',
    'final_winnings'  : final_winnings,
    'batting_winnings'  : batting_winnings,
    'bowling_winnings'  : bowling_winnings,
    'overall_winnings'  : overall_winnings,
    'sixes_winnings'  : sixes_winnings,
    'catches_winnings'  : catches_winnings,
    'max_points_winnings'  : max_points_winnings,
    'max_wickets_winnings'  : max_wickets_winnings,
    'matches': matches,
    'last_update_time': last_update_time
  }
  return render(request, "pages/winnings.html", context)
