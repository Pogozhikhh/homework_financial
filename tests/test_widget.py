import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card_type():
    pass

@pytest.mark.parametrize('value, expected', [
    ('2024-03-11T02:26:18.671407', '11.03.2024'),
    ('2024-08-06', '06.08.2024')
])


def test_get_date(value, expected):
    assert get_date(value) == expected



@pytest.mark.parametrize('value, expected', [
    ('20/12/2023', 'Некорректный формат даты'),
    ('06.05.2021', 'Некорректный формат даты'),
    ('двадцать второе июня сорок первого года', 'Некорректный формат даты'),
    ('aa-bb-cc', 'Некорректный формат даты'),
    ('', 'Некорректный формат даты')
])
def test_get_date_valueerror(value, expected):
    with pytest.raises(ValueError):
        get_date(value) == expected