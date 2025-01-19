import csv
from unittest.mock import mock_open, patch

import pandas as pd

from src.reading_financial_operation import read_file_csv, read_file_xlsx


def test_read_file_csv_correct_file():
    """Проверка на возврат нужного значения"""
    mock_csv_content = "name;amount;date\nJohn;100;2023-01-01\nJane;150;2023-01-02\n"
    expected_result = [
        {"name": "John", "amount": "100", "date": "2023-01-01"},
        {"name": "Jane", "amount": "150", "date": "2023-01-02"},
    ]

    with patch("builtins.open", mock_open(read_data=mock_csv_content), create=True):
        with patch("csv.DictReader", return_value=csv.DictReader(mock_csv_content.splitlines(), delimiter=";")):
            result = read_file_csv("fake_file.csv")
            assert result == expected_result


def test_read_file_csv_empty_filename():
    """Проверка что функция возвращает пустой список, если имя файла пустое."""
    assert read_file_csv("") == []


def test_file_not_found(mock_read_csv):
    """Проверка на ошибку ненайденного файла"""
    mock_read_csv.side_effect = FileNotFoundError
    result = read_file_csv("test_file.csv")
    assert result == []


@patch("pandas.read_excel")
def test_read_trans_xlsx(mock_read_excel):
    """Проверка на возврат нужного значения"""
    mock_data = [{"transaction_id": 1, "amount": 100}, {"transaction_id": 2, "amount": 200}]
    mock_read_excel.return_value = pd.DataFrame(mock_data)

    result = read_file_xlsx("test_file.xlsx")

    assert result == mock_data


def test_empty_filename():
    """Проверка что функция возвращает пустой список, если имя файла пустое."""
    result = read_file_xlsx("")
    assert result == []


@patch("pandas.read_excel")
def test_file_not_found(mock_read_excel):
    """Проверка на ошибку ненайденного файла"""
    mock_read_excel.side_effect = FileNotFoundError
    result = read_file_xlsx("test_file.xlsx")
    assert result == []
