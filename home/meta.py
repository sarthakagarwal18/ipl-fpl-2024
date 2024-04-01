import time
from . import google_sheets

cached_response1 = None
cached_response2 = None
last_call_time = None

def get_last_update_time():
    return google_sheets.fetch_sheet_data('Leaderboard!B5', 'ROWS')[0][0]

def get_matches():
    return google_sheets.fetch_sheet_data('Leaderboard!A7', 'ROWS')[0][0]

def get_meta():
    global cached_response1
    global cached_response2
    global last_call_time

    if last_call_time is None or cached_response1 is None or cached_response2 is None or (time.time() - last_call_time) > 60:
        last_call_time = time.time()
        cached_response1 = get_last_update_time()
        cached_response2 = get_matches()
    
    # Return the cached response
    return cached_response1, cached_response2
