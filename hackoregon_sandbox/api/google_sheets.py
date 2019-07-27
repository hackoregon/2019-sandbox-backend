import gspread
from oauth2client.service_account import ServiceAccountCredentials


CREDENTIALS_FILE = "FormTestProject-3c43acfaeacd.json"
LAYER_SHEET_NAME = 'CIVIC Sandbox - Layer Form (Responses)'
PACKAGE_SHEET_NAME = ''


def get_package_sheet_records():
    return get_sheet_records(PACKAGE_SHEET_NAME, CREDENTIALS_FILE)

def get_layer_sheet_records():
    return get_sheet_records(LAYER_SHEET_NAME, CREDENTIALS_FILE)
    

def get_sheet_records(name, credentials_file):
    SCOPE = ['https://www.googleapis.com/auth/spreadsheets.readonly', 'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, SCOPE)
    client = gspread.authorize(credentials)
    sheet = client.open(name).sheet1
    records = sheet.get_all_records()
    return records