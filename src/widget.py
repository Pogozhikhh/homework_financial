from typing import Any

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_card: Any) -> str:
    """Вывод замаскированных счетов и карт"""
    if type_card == "":
        raise ValueError('нет данных')
    else:
        if "Счет" in type_card:
            return "Счет " + get_mask_account(type_card[-16:])
        else:
            card = get_mask_card_number(type_card[-16:])
            correct_card = type_card.replace(type_card[-16:], card)
            return correct_card


def get_date(data: Any) -> str:
    """Функция преобразующая дату"""
    data_list = data.split('-')
    if data_list[0].isdigit() and data_list[1].isdigit() and data_list[2][:2].isdigit and len(data_list) == 3:
        returned_date = data_list[2][:2] + '.' + data_list[1] + '.' + data_list[0]
        return returned_date
    raise ValueError('Некорректный формат даты')


# print(mask_account_card("Maestro 1596837868705199"))
# print(mask_account_card("Счет 64686473678894779589"))
# print(mask_account_card("MasterCard 7158300734726758"))
# print(mask_account_card("Visa Classic 6831982476737658"))
# print(mask_account_card("Visa Platinum 8990922113665229"))
# print(get_date("2024-03-11T02:26:18.671407"))
