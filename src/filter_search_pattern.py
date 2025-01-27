import re
from collections import Counter
from typing import Any


def filter_banking_transactions_by_description(banking_description: list, search_bar: str) -> list:
    """Функция, возвращающая список, с содержанием указанной строки"""

    descr = []
    for description in banking_description:
        dict_str = str(description)
        if re.search(search_bar, dict_str, flags=re.IGNORECASE):
            descr.append(dict_str)
    return descr


def filter_banking_description(banking_description: list, category: list) -> dict:
    """Функция, возвращающая словарь, в котором ключи - это названия категорий, а значение - это количество операций"""
    string = []
    for categories in category:
        pattern = categories
        description = str(banking_description)
        string_ = re.findall(pattern, description, flags=re.IGNORECASE)
        string = string + string_

    result = dict(Counter(string))
    return result


def search_matches(list_dict: list, str_search: str) -> Any:
    """Функция принимает на вход список словарей и строку поиска и возвращает список словарей где найдены совпадения"""
    pattern = re.compile(str_search, flags=re.IGNORECASE)
    new_list = []
    for el in list_dict:
        for value in el.values():
            if pattern.search(str(value)):
                new_list.append(el)
            else:
                pass
    if not new_list:
        return "Совпадений не найдено!"
    else:
        return new_list
