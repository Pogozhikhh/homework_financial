from src.filter_search_pattern import filter_banking_description, filter_banking_transactions_by_description


def test_single_match_description():
    """Проверяет, что функция возвращает правильное количество операций для каждой категории, если есть одно
    совпадение."""
    banking_description = [
        {"description": "Payment for groceries"},
        {"description": "Payment for utilities"},
    ]
    result = filter_banking_description(banking_description, ["groceries", "utilities"])
    assert result == {"groceries": 1, "utilities": 1}


def test_multiple_matches_description():
    """Проверяет, что функция корректно считает количество совпадений для каждой категории."""
    banking_description = [
        {"description": "Payment for groceries"},
        {"description": "Payment for utilities"},
        {"description": "Transfer to groceries"},
    ]
    result = filter_banking_description(banking_description, ["groceries", "utilities"])
    assert result == {"groceries": 2, "utilities": 1}


def test_case_insensitivity_description():
    """Проверяет, что функция не чувствительна к регистру символов в описании."""
    banking_description = [
        {"description": "Payment for Groceries"},
        {"description": "Transfer to Savings"},
    ]
    result = filter_banking_description(banking_description, ["groceries"])
    assert result == {"Groceries": 1}


def test_empty_list_transactions():
    """Проверяет, что функция возвращает пустой список, если входной список пуст."""
    result = filter_banking_transactions_by_description([], "groceries")
    assert result == []


def test_no_matches_transactions():
    """Проверяет, что функция возвращает пустой список, если нет совпадений с поисковой строкой."""
    banking_description = [
        {"description": "Payment for groceries"},
        {"description": "Transfer to savings"},
    ]
    result = filter_banking_transactions_by_description(banking_description, "utilities")
    assert result == []


def test_single_match_transactions():
    """Проверяет, что функция возвращает правильный словарь, если есть одно совпадение."""
    banking_description = [
        {"description": "Payment for groceries"},
        {"description": "Payment for utilities"},
    ]
    result = filter_banking_transactions_by_description(banking_description, "groceries")
    assert result == ["{'description': 'Payment for groceries'}"]


def test_multiple_matches_transactions(transactions):
    """Проверяет, что функция возвращает все совпадения, если их несколько."""
    banking_description = [
        {"description": "Payment for groceries"},
        {"description": "Payment for utilities"},
        {"description": "Transfer to groceries"},
    ]
    result = filter_banking_transactions_by_description(banking_description, "groceries")
    expected = ["{'description': 'Payment for groceries'}", "{'description': 'Transfer to groceries'}"]
    assert result == expected


def test_case_insensitivity_transactions():
    """Проверяет, что функция корректно работает с учетом регистра символов."""
    banking_description = [
        {"description": "Payment for Groceries"},
        {"description": "Transfer to Savings"},
    ]
    result = filter_banking_transactions_by_description(banking_description, "groceries")
    assert result == ["{'description': 'Payment for Groceries'}"]
