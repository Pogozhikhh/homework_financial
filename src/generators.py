from typing import Any, Dict, Generator, Iterator, List


def check_key(dict_: dict, currency: str) -> bool:
    """Функция получает на вход словарь с данными о транзакций и валютой для сортировки,
    и возвращает если есть совпадение по валюте и присутствуют все ключи в словаре."""
    try:
        if dict_["operationAmount"]["currency"]["code"] == currency:
            return True
        else:
            return False
    except KeyError:
        return False


def filter_by_currency(transactions_list: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]] | str:
    """Функция возвращающая итератор, где валюта операции соответствует заданной"""
    filter_transactions = filter(lambda x: check_key(x, currency), transactions_list)

    for el in filter_transactions:
        yield el


def filter_by_currency_csv(transactions: list, currency: str) -> Any:
    for transaction in transactions:
        if transaction.get("currency_code") == currency:
            return transaction


def transaction_descriptions(transactions_list: List[Dict[str, Any]]) -> Any:
    """Функция, возвращающая итератор, где валюта операции соответствует заданной"""
    if not isinstance(transactions_list, list):
        raise TypeError("Ошибка типа данных")
    for transaction in transactions_list:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """Генератор номеров банковских карт в формате 'XXXX XXXX XXXX XXXX'"""
    if not isinstance(start, int) or not isinstance(stop, int):
        raise TypeError("Ошибка типа данных")
    if start > stop:
        raise ValueError("Границы диапазона указаны неверно")
    if len(str(start)) <= 16:
        for number in range(start, stop + 1):
            formated_card_number = "{:016}".format(number)
            yield " ".join(formated_card_number[i * 4 : (i + 1) * 4] for i in range(4))
    else:
        raise ValueError("Входные данные превышают допустимые значения!!!")
