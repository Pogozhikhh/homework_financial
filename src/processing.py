from datetime import datetime
from typing import Any, Iterable


def filter_by_state(list_of_dicts: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и значение для ключа и возвращает новый
    список содержащий только те словари у которых ключ содержит переданное значение"""
    return [t for t in list_of_dicts if t.get("state") == state]


def sort_by_date(list_of_dicts: Iterable[dict[str, Any]], reverse_list: bool = True) -> Iterable[dict[str, Any]]:
    """Функция принимает список и сортирует его по убыванию"""

    sorted_list = sorted(
        list_of_dicts, key=lambda strindate: datetime.fromisoformat(strindate["date"]), reverse=reverse_list
    )
    return sorted_list
