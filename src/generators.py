from typing import Any, Dict, Generator, Iterator, List

from tests.conftest import transactions


def filter_by_currency(transactions_list: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]] | str:
    """Функция возвращает итератор, выдающий транзакции, где валюта операции соответствует заданной"""
    if not isinstance(transactions_list, list) or not isinstance(currency, str):
        raise TypeError("Ошибка типа данных")

    if len(transactions_list) > 0:
        filter_info = filter(
            lambda x: x["operationAmount"]["currency"]["code"] == currency,
            transactions_list,
        )
        return filter_info
    else:
        return "Список пуст"


def transaction_descriptions(transactions_list: List[Dict[str, Any]]) -> Any:
    pass


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
