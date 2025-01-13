import os
from typing import Any
import pandas as pd

path_file = os.path.dirname(os.path.abspath(__file__))
path_file_csv = os.path.join(path_file, "../data/transactions.csv")
path_file_xlsx = os.path.join(path_file, "../data/transactions_excel.xlsx")

# with open(path_file_csv, encoding="utf-8") as file:
#     reader = pd.read_csv(file)
#     print(reader)


def read_file_csv(path_file_csv: str) -> Any:
    """Функция считывающая данные из CSV файла"""
    try:
        data_csv = pd.read_csv(path_file_csv, delimiter=":")
    except FileNotFoundError:
        return []
    read_data_csv = data_csv.to_dict(orient="records")
    return read_data_csv


def read_file_xlsx(path_file_xlsx: str) -> Any:
    """Функция считывающая данные из XLSX файла"""
    try:
        data_xlsx = pd.read_excel(path_file_xlsx)
        read_data_xlsx = data_xlsx.to_dict("records")
        if data_xlsx.empty:
            return "Файл пустой"
        else:
            return read_data_xlsx
    except FileNotFoundError:
        return []


# print(read_file_csv(path_file_csv))
# print(read_file_xlsx(path_file_xlsx))
