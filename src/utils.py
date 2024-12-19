import json
from json import JSONDecodeError

from src.external_api import conversion_currency


def prepare_json_file(json_file: str) -> dict | list:
    """Функция, преобразующая json файл в формат python"""
    try:
        with open(json_file, encoding="utf-8") as financial_file:
            try:
                transactions = json.load(financial_file)
            except JSONDecodeError:
                return []
        if not isinstance(transactions, list):
            return []
        return transactions
    except FileNotFoundError:
        return []


def transaction_amount(trans: dict, currency: str = "RUB") -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if trans["operationAmount"]["currency"]["code"] == currency:
        amount = trans["operationAmount"]["amount"]
    else:
        amount = conversion_currency(trans)
    return amount


# print(prepare_json_file(r"C:\Users\111\PycharmProjects\Poetry_Test\data\operations.json"))
# print(type(prepare_json_file(r"C:\Users\111\PycharmProjects\Poetry_Test\data\operations.json")))
