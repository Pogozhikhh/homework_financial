import logging
import os

from src.filter_search_pattern import search_matches
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.reading_financial_operation import read_file_csv, read_file_xlsx
from src.utils import prepare_json_file
from src.widget import mask_account_card

path_file = os.path.dirname(os.path.abspath(__file__))
path_file_json = os.path.join(path_file, "../data/operations.json")
path_file_csv = os.path.join(path_file, "../data/transactions.csv")
path_file_xlsx = os.path.join(path_file, "../data/transactions_excel.xlsx")

rel_file_path = os.path.join(path_file, "../logs/main.log")
abs_file_path = os.path.abspath(rel_file_path)
logger = logging.getLogger("main")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(abs_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def main():
    """Функция, отвечающая за общую логику программы"""
    global use_file
    print(
        "Привет! Добро пожаловать в программу работы \n"
        "с банковскими транзакциями. \n"
        "Выберите необходимый пункт меню:"
    )

    input_choice = ["1", "2", "3"]

    print(
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла\n"
    )

    user_input_file = ""
    while user_input_file not in input_choice:
        user_input_file = input("Введите номер: ")

    use_file = []

    if user_input_file == 1:
        logger.info("Выбран файл формата: JSON")
        print("Для обработки выбран JSON-файл.")
        use_file = prepare_json_file(path_file_json)
    elif user_input_file == 2:
        logger.info("Выбран файл формата: CSV")
        print("Для обработки выбран CSV-файл.")
        use_file = read_file_csv(path_file_csv)
    elif user_input_file == 3:
        logger.info("Выбран файл формата: XLSX")
        print("Для обработки выбран XLSX-файл.")
        use_file = read_file_xlsx(path_file_xlsx)
    else:
        print("Введен некорректный номер")

    user_use_status = input(
        "Введите статус, по которому необходимо выполнить фильтрацию. \n"
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING. \n"
        "Введите статус: "
    ).upper()
    while user_use_status != "EXECUTED" and user_use_status != "CANCELED" and user_use_status != "PENDING":
        logger.error("Введен неправильный статус")
        print(f'Статус операции "{user_use_status}" недоступен.')
        user_use_status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию. \n"
            "            Доступные для фильтровки статусы: \n"
            "            EXECUTED, CANCELED, PENDING\n"
            "            :"
        )
        user_use_status = user_use_status.upper()
    else:
        if user_use_status == "EXECUTED":
            logger.info("Выбран статус : EXECUTED")
            print('Операции отфильтрованы по статусу "EXECUTED"')
        elif user_use_status == "CANCELED":
            logger.info("Выбран статус : CANCELED")
            print('Операции отфильтрованы по статусу "CANCELED"')
        else:
            logger.info("Выбран статус : PENDING")
            print('Операции отфильтрованы по статусу "PENDING"')

    filter_trans = filter_by_state(use_file, user_use_status)

    data_filter = input("Отсортировать операции по дате? Да/Нет:").lower()

    if data_filter == "да":

        sort = input("Отсортировать по возрастанию или по убыванию?:")
        sort = sort.lower()
        if sort == "по возрастанию":
            sort_key = False
        else:
            sort_key = True

        new_filter_trans = sort_by_date(filter_trans, sort_key)
    else:
        new_filter_trans = filter_trans

    code = input("Выводить только рублевые тразакции? Да / Нет:")

    code = code.upper()

    if code == "ДА":
        new_filter_trans = filter_by_currency(list(new_filter_trans), "RUB")

    filter_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").upper()

    if filter_word == "ДА":
        logger.info("Выбран поиск по слову")
        word = input("Введите слово по которому пройдет фильтрация: ")
        logger.info(f"Поиск происходит по слову{word}")
        cor_filter_word = search_matches(list(new_filter_trans), word)

        if cor_filter_word == "Совпадений не найдено!":
            logger.info(f"Поиск не нашел слово: {word}, ")
            print("Совпадений не найдено!")
            cor_filter_word = new_filter_trans
    else:
        cor_filter_word = list(new_filter_trans)

    print("Распечатываю итоговый список транзакций...")

    if len(list(new_filter_trans)) == 0:
        logger.info("Нет подходящих данных по поиску")
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    print(f"Всего банковских операций в выборке: {len(cor_filter_word)}")

    for el in cor_filter_word:
        if el.get("operationAmount"):
            if el.get("from"):
                print(
                    f"{el['date']} {el['description']}\n"
                    f"{mask_account_card(el['from'])} -> {mask_account_card(el['to'])}\n"
                    f"Сумма: {el['operationAmount']['amount']} {el['operationAmount']['currency']['name']}\n"
                )
            else:
                print(
                    f"{el['date']} {el['description']}\n"
                    f"{mask_account_card(el['to'])}\n"
                    f"Сумма: {el['operationAmount']['amount']} {el['operationAmount']['currency']['name']}\n"
                )
        else:
            if el.get("from") and type(el["from"]) is not float:
                print(
                    f"{el['date']} {el['description']}\n"
                    f"{mask_account_card(el['from'])} -> {mask_account_card(el['to'])}\n"
                    f"Сумма: {el['amount']} {el['currency_name']}\n"
                )
            else:
                print(
                    f"{el['date']} {el['description']}\n"
                    f"{mask_account_card(el['to'])}\n"
                    f"Сумма: {el['amount']} {el['currency_name']}\n"
                )


if __name__ == "__main__":
    main()
