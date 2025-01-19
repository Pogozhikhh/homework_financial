import csv
import logging
import os
from typing import Any

import pandas as pd

path_file = os.path.dirname(os.path.abspath(__file__))
path_file_csv = os.path.join(path_file, "../data/transactions.csv")
path_file_xlsx = os.path.join(path_file, "../data/transactions_excel.xlsx")


rel_file_path = os.path.join(path_file, "../logs/reading_financial_operation.log")
abs_file_path = os.path.abspath(rel_file_path)

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(abs_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_file_csv(filename: str) -> list:
    """Функция считывающая данные из CSV файла"""
    if len(filename) == 0 or not isinstance(filename, str):
        return []
    try:
        logger.info("Открытие файла формата CSV")
        with open(filename, encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            return list(reader)
    except FileNotFoundError as error:
        logger.error(f"Ошибка чтения файла {error}")
        return []


def read_file_xlsx(path_file_xlsx: str) -> Any:
    """Функция считывающая данные из XLSX файла"""
    try:
        logger.info("Открытие файла формата XLSX")
        data_xlsx = pd.read_excel(path_file_xlsx)
        read_data_xlsx = data_xlsx.to_dict("records")
        if data_xlsx.empty:
            return "Файл пустой"
        else:
            return read_data_xlsx
    except FileNotFoundError as error:
        logger.error(f"Ошибка чтения файла {error}")
        return []


# print(read_file_csv(path_file_csv))
# print(read_file_xlsx(path_file_xlsx))
