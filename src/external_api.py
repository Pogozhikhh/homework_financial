import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
values = os.getenv("API-KEY")


def conversion_currency(transactions: Any) -> Any:
    """Функция конвертации"""
    amount = transactions["operationAmount"]["amount"]
    code = transactions["operationAmount"]["currency"]["code"]
    to = "RUB"
    if code == "RUB":
        return float(amount)
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={code}&amount={amount}"
        payload = {}
        response = requests.get(url, headers={"apikey": values}, data=payload)
        status_code = response.status_code
        if status_code == 200:
            result = response.json()
            return result["result"]
        else:
            print(f"Запрос не был успешным. Возможная причина: {response.reason}")
