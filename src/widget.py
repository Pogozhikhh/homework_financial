from masks import get_mask_card_number, get_mask_account


def mask_account_card(type_card: str) -> str:
    """Вывод замаскированных счетов и карт"""

    if "Счет" in type_card:
        return "Счет" + get_mask_account(type_card)
    else:
        card = get_mask_card_number(type_card[-16:])
        correct_card = type_card.replace(type_card[-16:], card)
        return correct_card


def get_date(incorrect_data: str) -> str:
    """Функция преобразующая дату"""
    pass


print(mask_account_card("Maestro 1596837868705199"))
