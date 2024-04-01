from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'service_account.json'
SPREADSHEET_ID = '1Qex3w6Po8WF8jtznaNtkmzBPAB_vk_YJxkhJ0ivxqRE'

credentials = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('sheets', 'v4', credentials=credentials)

# Function to fetch sheets data
def fetch_sheet_data(range_name, majorDimension):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=range_name, majorDimension=majorDimension).execute()
    result['values'] = [[item.replace('Farzi', 'Sarthak') if 'Farzi' in item else item for item in sublist] 
                  for sublist in result['values']]
    return result.get('values', [])