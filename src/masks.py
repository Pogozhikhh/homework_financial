def get_mask_card_number(card_number: int) -> str:
    """Возвращает замаскированный номер карты"""
    if isinstance(card_number, int):
        card_number_str = str(card_number)  # перевод числа в строку
        if len(card_number_str) < 12:
            raise ValueError('Некорректный номер карты')
        return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
    else:
        raise TypeError('Некорректный тип данных')

def get_mask_account(card_number: int) -> str:
    """Возвращает замаскированные последние числа карты"""
    if isinstance(card_number, int):
        card_number_str = str(card_number)  # перевод числа в строку
        if len(card_number_str) == 12:
            return f"**{card_number_str[-4:]}"
        else:
            raise ValueError('Неправильная длина номера')
    else:
        raise TypeError('Неправильный тип данных')

# print(get_mask_card_number(123456789012))
# print(get_mask_account(123456789012))
