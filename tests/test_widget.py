import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card_type():
    pass


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == '11.03.2024'
