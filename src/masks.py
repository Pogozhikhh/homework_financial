from typing import Any


def get_mask_card_number(card_number: Any) -> str:
    """Возвращает замаскированный номер карты"""
    card_number_str = str(card_number)  # перевод числа в строку
    if 12 <= len(card_number_str) <= 20:
        masked_card = card_number_str[:4] + " " + card_number_str[4:6] + "** **** " + card_number_str[-4:]
        return str(masked_card)
    raise ValueError("Некорректный номер карты")


def get_mask_account(card_number: Any) -> str:
    """Возвращает замаскированные последние числа карты"""
    card_number_str = str(card_number)  # перевод числа в строку
    if card_number_str.isdigit() and 12 <= len(card_number_str) <= 20:
        return f"**{card_number_str[-4:]}"
    raise ValueError("Неправильная длина номера")


# print(get_mask_card_number(123456789012))
# print(get_mask_account(12345678901234567890))
