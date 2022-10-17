import os
import requests
import json

# Gets api key
api_key = os.environ.get("API_KEY")


def exchange(currency1, currency2, amount):

    # Url used for this function
    url = f"https://api.apilayer.com/currency_data/convert?to={currency2}&from={currency1}&amount={amount}"

    payload = {}
    headers = {
        "apikey": api_key
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.text

    # Converts data into a dictionary
    result = json.loads(result)
    finale = result["result"]

    return finale


def currency_list():

    # Url used for this function
    url = "https://api.apilayer.com/currency_data/list"

    payload = {}
    headers = {
        "apikey": api_key
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    result = response.text
    result = json.loads(result)
    # Converts data into a dictionary
    finale = list(result["currencies"].keys())
    return finale


def temp_currency_list():
    # A function made for testing over and over since I had limited requests with the actual api
    ls = ["XOF", "XPF", "YER", "ZAR", "ZMK", "ZMW", "ZWL"]
    return ls

