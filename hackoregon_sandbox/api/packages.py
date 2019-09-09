import json


def load_json_from_file(json_file_path):
    with open(json_file_path) as json_file:
        json_data = json.load(json_file)
        return json_data