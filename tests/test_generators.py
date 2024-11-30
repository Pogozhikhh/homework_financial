import pytest

from src.generators import card_number_generator

@pytest.mark.parametrize('start, stop, expected', [(10, 12, ["0000 0000 0000 0010",
                                                             "0000 0000 0000 0011",
                                                             "0000 0000 0000 0012"]),
                                                   (5, 6, ["0000 0000 0000 0005",
                                                           "0000 0000 0000 0006"]),
                                                   (1000, 1002, ["0000 0000 0000 1000",
                                                                 "0000 0000 0000 1001",
                                                                 "0000 0000 0000 1002"])])
def test_card_number_generator(start, stop, expected):
    result = card_number_generator(start, stop)
    assert next(result) == expected[0]
    assert next(result) == expected[1]


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
