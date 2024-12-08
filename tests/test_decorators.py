import pytest

from src.decorators import log


@log(filename="mylog.txt")
def my_function(x: int | str, y: int | str):
    """Функция суммирует два числа и возвращает результат"""
    try:
        return int(x) + int(y)
    except ValueError as e:
        print("Ошибка ввода! Пожалуйста, вводите только целые числа.")
        raise e


def test_log_save_file():
    positive_result = my_function(2, 2)
    assert positive_result == 4


def test_log_captured(capsys):
    @log(filename=None)
    def my_function(x: int, y: int) -> int:
        """Функция суммирует два числа и возвращает результат"""
        return x + y

    my_function(2, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"
