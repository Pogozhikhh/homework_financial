import logging
import os.path
from typing import Any

current_dir = os.path.dirname(os.path.abspath(__file__))

rel_file_path = os.path.join(current_dir, "../logs/masks.log")
abs_file_path = os.path.abspath(rel_file_path)

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(rel_file_path,"w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Any) -> str:
    """Возвращает замаскированный номер карты"""
    card_number_str = str(card_number)  # перевод числа в строку
    if 12 <= len(card_number_str) <= 20:
        masked_card = card_number_str[:4] + " " + card_number_str[4:6] + "** **** " + card_number_str[-4:]
        logger.info("Возвращение замаскированного номера карты в формате '1234 56** **** 3456'")
        return str(masked_card)
    raise ValueError("Некорректный номер карты")


def get_mask_account(card_number: Any) -> str:
    """Возвращает замаскированные последние числа карты"""
    card_number_str = str(card_number)  # перевод числа в строку
    if card_number_str.isdigit() and 12 <= len(card_number_str) <= 20:
        logger.info("Возвращение замаскированного номера карты")
        return f"**{card_number_str[-4:]}"
    raise ValueError("Неправильная длина номера")


print(get_mask_card_number(123456789012))
print(get_mask_account(12345678901234567890))