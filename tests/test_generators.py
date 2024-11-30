import pytest

from src.generators import card_number_generator


def test_card_number_generator_type():
    with pytest.raises(TypeError):
        next(card_number_generator([1, 2, 3], 3))
    with pytest.raises(TypeError):
        next(pytest.raises("12345", 1))


def test_card_number_generator_len():
    with pytest.raises(ValueError):
        next(card_number_generator(10000000000000000, 10000000000000001))


def test_card_number_generator_after_boundary_values():
    with pytest.raises(ValueError):
        next(card_number_generator(10000000000000000, 10000000000000001))


def test_card_number_generator_wrong_start_stop():
    with pytest.raises(ValueError):
        next(card_number_generator(7, 5))
