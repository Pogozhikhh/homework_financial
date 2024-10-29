from masks import get_mask_account, get_mask_card_number


def mask_account_card(type_card: str) -> str:
    """Вывод замаскированных счетов и карт"""

    if "Счет" in type_card:
        return "Счет " + get_mask_account(type_card)
    else:
        card = get_mask_card_number(type_card[-16:])
        correct_card = type_card.replace(type_card[-16:], card)
        return correct_card


def get_date(data: str) -> str:
    """Функция преобразующая дату"""

    return f"{data[8:10]}.{data[5:7]}.{data[0:4]}"


# print(mask_account_card("Maestro 1596837868705199"))
# print(mask_account_card("Счет 64686473678894779589"))
# print(mask_account_card("MasterCard 7158300734726758"))
# print(mask_account_card("Visa Classic 6831982476737658"))
# print(mask_account_card("Visa Platinum 8990922113665229"))
# print(get_date("2024-03-11T02:26:18.671407"))
