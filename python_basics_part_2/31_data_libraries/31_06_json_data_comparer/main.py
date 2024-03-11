import json


def load_json(file_path: str) -> dict:
    """ Loads data from a JSON file. """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def find_differences(old_json_data: dict, new_json_data: dict, keys_to_compare: list) -> dict:
    """ Finds differences between two dictionaries for specified keys. """
    diffs = {}
    for key in keys_to_compare:
        if old_json_data.get(key) != new_json_data.get(key):
            diffs[key] = new_json_data[key]
    return diffs


def save_json(data_to_save: dict, file_path: str):
    """ Saves data to a JSON file. """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data_to_save, file, indent=4)


json_old_path = 'json_old.json'
json_new_path = 'json_new.json'
diff_list = ['services', 'staff', 'datetime']

old_data = load_json(json_old_path)
new_data = load_json(json_new_path)

differences = find_differences(old_data['data'], new_data['data'], diff_list)

print(differences)
save_json(differences, 'result.json')
