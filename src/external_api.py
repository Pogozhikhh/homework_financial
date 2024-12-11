import requests
import os
from dotenv import load_dotenv
from typing import Any



load_dotenv()
values = os.getenv("API-KEY")
def conversion_currency(transactions: Any) -> Any:
    """Функция конвертации"""
    amount = transactions["operationAmount"]["amount"]
    code = transactions["operationAmount"]["currency"]["code"]
    to = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={code}&amount={amount}"
    payload = {}
    response = requests.get(url, headers={"apikey": values}, data=payload)
    result = response.json()
    return result["result"]
