import os
from unittest.mock import patch

import pytest

from src.utils import prepare_json_file, transaction_amount


@pytest.fixture
def path():
    path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
    return path_to_file


@pytest.fixture
def path_empty_list():
    path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations_1.json")
    return path_to_file


@pytest.fixture
def trans():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@pytest.fixture
def trans_1():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


def test_financial_transactions(path):
    assert prepare_json_file(path)[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


def test_prepare_json_file_empty():
    assert prepare_json_file("empty") == []


def test_financial_transactions_empty_list(path_empty_list):
    assert prepare_json_file(path_empty_list) == []


def test_transaction_amount(trans):
    assert transaction_amount(trans) == "31957.58"


@patch("src.utils.conversion_currency")
def test_transaction_amount_not_rub(mock_conversion_currency, trans_1):
    mock_conversion_currency.return_value = 1000.0
    assert transaction_amount(trans_1) == 1000.0
