import requests
import json


def get_stock_price(stock_name, token):
    stock_name = stock_name.upper()
    url = f"https://realstonks.p.rapidapi.com/{stock_name}"
    headers = {
        "X-RapidAPI-Host": "realstonks.p.rapidapi.com",
        "X-RapidAPI-Key": f"{token}"
    }
    response = requests.request("GET", url, headers=headers)

    if response.status_code == 404:
        return f"{stock_name} não está listado na Nasdaq."

    stock_data = json.loads(response.text) 
    return f"As ações de {stock_name} estão custando ${stock_data['price']}."
