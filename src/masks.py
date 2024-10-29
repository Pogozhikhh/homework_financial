def get_mask_card_number(card_number: int) -> str:
    """Возвращает замаскированный номер карты"""
    card_number_str = str(card_number)  # перевод числа в строку
    return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"


def get_mask_account(card_number: int) -> str:
    """Возвращает замаскированные последние числа карты"""
    card_number_str = str(card_number)  # перевод числа в строку
    return f"**{card_number_str[-4:]}"


# print(get_mask_card_number(123456789012))
# print(get_mask_account(123456789012))
