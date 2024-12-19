import json

from src.external_api import conversion_currency


def prepare_json_file(json_file: str) -> dict | list:
    """Функция, преобразующая json файл в формат python"""
    empty_list = []
    if json_file is not list and len(json_file) > 0:
        with open(json_file, "r", encoding="utf-8") as f:
            transactions = json.load(f)
            return transactions
    else:
        return empty_list


def transaction_amount(trans: dict, currency: str = "RUB") -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if trans["operationAmount"]["currency"]["code"] == currency:
        amount = trans["operationAmount"]["amount"]
    else:
        amount = conversion_currency(trans)
    return amount


# print(prepare_json_file(r"C:\Users\111\PycharmProjects\Poetry_Test\data\operations.json"))
# print(type(prepare_json_file(r"C:\Users\111\PycharmProjects\Poetry_Test\data\operations.json")))

