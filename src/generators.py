from typing import Any, Dict, Generator, List, Union

from tests.conftest import transactions


def filter_by_currency(info: Union[list, dict], currency: str) -> Any:
    pass


def transaction_descriptions(info: List[Dict[str, Any]]):
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