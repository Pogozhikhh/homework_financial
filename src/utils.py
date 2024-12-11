import json


def prepare_json_file(json_file: str) -> dict | list:
    ''' Функция, преобразующая json файл в формат python'''
    empty_list = []
    if json_file is not list and len(json_file) > 0:
        with open(json_file, 'r', encoding="utf-8") as f:
            transactions = json.load(f)
            return transactions
    else:
        return empty_list

print(prepare_json_file(r'C:\Users\111\PycharmProjects\Poetry_Test\data\operations.json'))
print(type(prepare_json_file(r'C:\Users\111\PycharmProjects\Poetry_Test\data\operations.json')))
