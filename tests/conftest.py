import pytest


@pytest.fixture
def test_dict_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def test_dict_list_incorrect_date():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03"},
        {"id": 939719570, "state": "EXECUTED", "date": "30.06.2018"},
        {"id": 594226727, "state": "CANCELED", "date": "12/09/2017 21;42"},
        {"id": 615064591, "state": "CANCELED", "date": "четырнадцатое октября две тысячи восемнадцатого года"},
    ]


@pytest.fixture
def test_dict_list_incorrect_date_second_version():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03"},
        {"id": 615064591, "state": "CANCELED", "date": "четырнадцатое октября две тысячи восемнадцатого года"},
        {"id": 939719570, "state": "EXECUTED", "date": "30.06.2018"},
        {"id": 594226727, "state": "CANCELED", "date": "12/09/2017 21;42"},
    ]
