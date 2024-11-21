import pytest


from src.widget import mask_account_card


def test_mask_account_card_type():
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"


def test_get_date():
    pass
