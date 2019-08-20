import gspread
from oauth2client.service_account import ServiceAccountCredentials


CREDENTIALS_FILE = "src_files/credentials.json"
SCOPE = ['https://www.googleapis.com/auth/spreadsheets.readonly', 'https://www.googleapis.com/auth/drive']
CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, SCOPE)

LAYER_RESPONSE_SHEET_NAME = 'CIVIC Sandbox - Layer Form (Responses)'
LAYER_RESPONSE_SHEET_INDEX = 1

PACKAGE_RESPONSE_SHEET_NAME = 'Package Creation Form (Responses)'
PACKAGE_RESPONSE_SHEET_INDEX = 0

"""

"""
# def create_layer_from_last_response_row():    
#     last_row_dictionary = get_last_row_dictionary(LAYER_RESPONSE_SHEET_NAME, LAYER_RESPONSE_SHEET_INDEX)
#     new_layer = models.Layer()
#     return new_layer


def main():
    last_row_dictionary = get_layer_last_row_dictionary()
    return last_row_dictionary


"""

"""
def get_layer_last_row_dictionary():
    return get_last_row_dictionary(LAYER_RESPONSE_SHEET_NAME, LAYER_RESPONSE_SHEET_INDEX)


"""

"""
def get_layer_row_dictionary(row_index):
    return get_row_as_dictionary(LAYER_RESPONSE_SHEET_NAME, LAYER_RESPONSE_SHEET_INDEX, row_index)

"""

"""
def get_package_row_dictionary(row_index):
    return get_row_as_dictionary(PACKAGE_RESPONSE_SHEET_NAME, PACKAGE_RESPONSE_SHEET_INDEX, row_index)


"""

"""
def get_worksheet(name, index):    
    client = gspread.authorize(CREDENTIALS)
    spreadsheet = client.open(name)
    worksheet = spreadsheet.get_worksheet(index)            
    return worksheet


"""

"""
def get_all_records(worksheet_name, worksheet_index):
    worksheet = get_worksheet(worksheet_name, worksheet_index)
    all_records = worksheet.get_all_records()
    return all_records


"""

"""
def get_row_as_dictionary(worksheet_name, worksheet_index, row_index):
    all_records = get_all_records(worksheet_name, worksheet_index)
    try:
        row_dictionary = all_records[row_index]
        return row_dictionary
    except KeyError:   
        return None


"""

"""
def get_last_row_index(worksheet_name, worksheet_index):
    worksheet = get_worksheet(worksheet_name, worksheet_index)
    all_values = worksheet.get_all_values()
    last_row_index = len(all_values)-1
    last_row_index -= 1 # first row is the column headers
    return last_row_index


"""

"""
def get_last_row_dictionary(worksheet_name, worksheet_index):
    last_row_index = get_last_row_index(worksheet_name, worksheet_index)
    last_row_dictionary = get_row_as_dictionary(worksheet_name, worksheet_index, last_row_index)
    return last_row_dictionary

#"""
#
#"""
# def get_row_values(worksheet_name, index):    
#     worksheet = get_worksheet(worksheet_name, index)
#     if index < worksheet.row_count:
#         row_values = worksheet.row_values(index)
#         return row_values
#     else:
#         return []

if __name__ == '__main__':    
    last_row_dictionary = main()