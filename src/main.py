import os
from src.reading_financial_operation import read_file_csv, read_file_xlsx
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from src.utils import prepare_json_file

path_file = os.path.dirname(os.path.abspath(__file__))
path_file_json = os.path.join(path_file, "../data/operations.json")
path_file_csv = os.path.join(path_file, "../data/transactions.csv")
path_file_xlsx = os.path.join(path_file, "../data/transactions_excel.xlsx")


def get_info_transaction():
    print("""Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:""")

    user_choise = int(input("""1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""))

    if user_choise == 1:
        print("Для обработки выбран JSON-файл.")
        choise_file = prepare_json_file(path_file_json)
        return choise_file
    elif user_choise == 2:
        print("Для обработки выбран CSV-файл.")
        choise_file = read_file_csv(path_file_csv)
        return choise_file
    elif user_choise == 3:
        print("Для обработки выбран XLSX-файл.")
        choise_file = read_file_xlsx(path_file_xlsx)
        return choise_file
    else:
        return "Введен некорректный номер"

def filter_status(user_file):
    while True:
        print("""Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
        user_choise_status = input("Введите статус: ").upper()

        if user_choise_status in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Операции отфильтрованы по статусу {user_choise_status}")
            result_choise_status = filter_by_state(user_file, user_choise_status)
            break
        else:
            print(f"Статус операции {user_choise_status} недоступен.")
    return result_choise_status


if __name__ == "__main__":
    file_choise = get_info_transaction()
    print(file_choise)