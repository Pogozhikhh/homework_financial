import json
import logging
import os.path
from json import JSONDecodeError

from src.external_api import conversion_currency

current_dir = os.path.dirname(os.path.abspath(__file__))

rel_file_path = os.path.join(current_dir, "../logs/utils.log")
abs_file_path = os.path.abspath(rel_file_path)

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(abs_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def prepare_json_file(json_file: str) -> dict | list:
    """Функция, преобразующая json файл в формат python"""
    try:
        logger.info(f"Получение данных из файла '{json_file}'")
        with open(json_file, encoding="utf-8") as financial_file:
            try:
                transactions = json.load(financial_file)
            except JSONDecodeError as jde:
                logger.error(f"Ошибка при чтении файла '{jde}'")
                return []
        if not isinstance(transactions, list):
            return []
        return transactions
    except FileNotFoundError as fnef:
        logger.error(f"Ошибка: Файл '{fnef}' не найден")
        return []


def transaction_amount(trans: dict, currency: str = "RUB") -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    logger.info("Получение суммы транзакций")
    if trans["operationAmount"]["currency"]["code"] == currency:
        amount = trans["operationAmount"]["amount"]
    else:
        amount = conversion_currency(trans)
    return amount


print(prepare_json_file(r"C:\Users\111\PycharmProjects\Poetry_Test\data\operations.json"))
print(type(prepare_json_file(r"C:\Users\111\PycharmProjects\Poetry_Test\data\operations.json")))
