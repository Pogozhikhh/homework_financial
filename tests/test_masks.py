import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    """Проверка корректной маскировки номера карты"""
    assert get_mask_card_number(123456789012) == "1234 56** **** 9012"
    assert get_mask_card_number(210987654321) == "2109 87** **** 4321"


def test_get_mask_card_number_len():
    """Проверка корректной длины карты"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(1234567890)

    assert str(exc_info.value) == "Некорректный номер карты"


def test_get_mask_card_number_type():
    """ Проверка корректного типа данных"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("1234567890")

    assert str(exc_info.value) == "Некорректный номер карты"


def test_get_mask_account():
    """Проверка правильности маскировки"""
    assert get_mask_account(123456789012) == "**9012"
    assert get_mask_account(198765432112) == "**2112"


def test_get_mask_account_type():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account("12345")

    assert str(exc_info.value) == "Неправильная длина номера"


def test_get_mask_account_len():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(1234567890)

    assert str(exc_info.value) == "Неправильная длина номера"
