from . import google_sheets

def get_data(range, majorDimension):
    return google_sheets.fetch_sheet_data('Leaderboard!' + range, majorDimension)

def create_dictionaries(data_pairs):
    dictionaries = []
    for i in range(0, len(data_pairs), 2):
        key_values = data_pairs[i]
        values = data_pairs[i + 1]

        filtered_pairs = [(key, value) for key, value in zip(key_values, values) if value != '']
        if not filtered_pairs:
            continue
        keys, values = zip(*filtered_pairs)
        values = list(map(float, values))
        dictionaries.append(dict(zip(keys, values)))
    return dictionaries

def create_tuples(data_pairs):
    all_tuples = []
    # Iterate through each pair of lists (one iteration handles a key list and a value list)
    for i in range(0, len(data_pairs), 2):
        key_values = data_pairs[i]
        value_strings = data_pairs[i + 1]

        # Process each key-value pair in the current lists
        current_tuples = [(key, float(value)) for key, value in zip(key_values, value_strings) if value != '']

        # Append the current list of tuples for this pair of columns to the main list
        all_tuples.append(current_tuples)
    
    return all_tuples