# Домашняя работа 13.2
## Цель проекта
### Написать функцию "main" в модуле main , которая отвечает за основную логику проекта и связывает функциональности между собой.**

## Инструкция по установке
1. ### Клонируйте репозиторий:
```
git clone https://github.com/Pogozhikhh/homework_financial.git
```
2. ### Установите зависимости:
```
pip install -r requirements.txt
```
## Новые фичи
### В домашнем задании добавлен модуль ***processing***, в котором реализованы две функции:

* ***filter_by_state()***
* ***sort_by_date()***

### 1.  Функция ***filter_by_state()*** принимает список словарей и опционально значение для ключа **'state'** (по умолчанию ***'EXECUTED'***). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ **'state'** соответствует указанному значению.

### 2. Функция ***sort_by_date()*** принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание). Функция возвращает новый список, отсортированный по дате **('date')**.

## Примеры использования функций
### Функция ***filter_by_state()***
### **Пример входных данных для функции**
```
[
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]
```

## **Пример работы функции**
### **Выход функции со статусом по умолчанию ***'EXECUTED'*****
```
[
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
]
```
### **Выход функции, если вторым аргументов передано ***'CANCELED'*****
```
[
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]
```
## Функция ***sort_by_date()***
### **Пример входных данных для функции**
```
[
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]
```
## Пример работы функции
### **Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)**
```
[
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
]
```
### В домашнем задании добавлен модуль ***generators***, в котором реализованы три функции:

* ***filter_by_currency()***
* ***transaction_descriptions()***
* ***card_number_generator()***

### 1. Функция ***filter_by_currency()*** которая принимает на вход список словарей, представляющих транзакции и возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD).

### 2. Функция ***transaction_descriptions()*** Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.

### 3. Функция ***card_number_generator()*** Генератор, который выдает номера банковских карт в формате "XXXX XXXX XXXX XXXX"

## Функция ***filter_by_currency()***
### **Пример входных данных для функции**
```
{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
```
## Функция ***transaction_descriptions()***
### **Пример входных данных для функции**
```
{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
```
## Пример работы функции
### **Выход функции**
```
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

>>> Перевод организации
```
## Функция ***card_number_generator()***

## Пример работы функции
### **Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)**
```
for card_number in card_number_generator(1, 5):
    print(card_number)

>>> 0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005
```

## Добавление модуля ***decorators*** с добавлением функции ***log***
```def log(filename):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename is not None:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} ok")
                else:
                    print(f"{func.__name__} ok")
                return result
            except TypeError as e:
                if filename is not None:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                raise e

        return wrapper

    return decorator
```

## Добавление модуля ***filter_search_pattern*** с добавлением функций ***filter_banking_transactions_by_description*** ,***filter_banking_description*** , ***search_matches*** 

## Функция ***filter_banking_transactions_by_description***
```
"""Функция, возвращающая список, с содержанием указанной строки"""

    descr = []
    for description in banking_description:
        dict_str = str(description)
        if re.search(search_bar, dict_str, flags=re.IGNORECASE):
            descr.append(dict_str)
    return descr
```
## Функция ***filter_banking_description***
```
"""Функция, возвращающая словарь, в котором ключи - это названия категорий, а значение - это количество операций"""
    string = []
    for categories in category:
        pattern = categories
        description = str(banking_description)
        string_ = re.findall(pattern, description, flags=re.IGNORECASE)
        string = string + string_

    result = dict(Counter(string))
    return result
```
## Функция ***search_matches***
```
"""Функция принимает на вход список словарей и строку поиска и возвращает список словарей где найдены совпадения"""
    pattern = re.compile(str_search, flags=re.IGNORECASE)
    new_list = []
    for el in list_dict:
        for value in el.values():
            if pattern.search(str(value)):
                new_list.append(el)
            else:
                pass
    if not new_list:
        return "Совпадений не найдено!"
    else:
        return new_list
```

## Тестирование
### Тестами покрыто 91% кода. Все тесты завершаются ожидаемым образом
