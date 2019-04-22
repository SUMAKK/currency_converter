import requests
import json
import argparse


def get_currency_code(symbol):
    """
    Method get symbol of currency and return currency code.

    :param symbol: currency symbol E.g.($,€)
    :return: currency code E.g.(USD,EUR)
    """
    try:
        url = "http://www.localeplanet.com/api/auto/currencymap.json"
        result = requests.get(url)
    except:
        return None
    currency_symbols = dict(result.json())
    for key, value in currency_symbols.items():
        if symbol == value['symbol']:
            return key


def get_rate(input_currency, output_currency):
    """
    Method try get currency rates from api.

    :param input_currency: (str) the currency we are onverting from
    :param output_currency:(str) optional prameter (when None return all rates)
    :return: return json object with all requested rates.
    """
    if input_currency is None:
        input_currency = ""
    if output_currency is None:
        url = "https://api.exchangeratesapi.io/latest?base=" + input_currency
    else:
        url = "https://api.exchangeratesapi.io/latest?base=" + input_currency + "&symbols=" + output_currency
    try:
        result = requests.get(url)
        if result.status_code == 200:
            return result.json()
        else:
            return None
    except:
        return None


def currency_converter(amount, input_currency, output_currency):
    """
    Method convert amount of some input currency into output currency/s.

    :param amount: (float) amount of the currency we are converting from.
    :param input_currency: (str) the currency we are converting from.
    :param output_currency: (str) optional prameter (when None return all rates)
    :return: return all required converted currencies.
    """
    try:
        amount = float(amount)
    except:
        return "Amount parameter is't float or int."
    if len(input_currency) < 3 or len(input_currency) > 3:
        input_currency = get_currency_code(input_currency)
    if output_currency is not None:
        if len(output_currency) < 3 or len(output_currency) > 3:
            output_currency = get_currency_code(output_currency)
    rates = get_rate(input_currency, output_currency)
    if rates is not None:
        rates = rates['rates']
        data = {}
        for rate in rates.items():
            c = rate[0]
            r = round(rate[1] * abs(amount), 2)
            data.update({c: r})
        output = {
            "input":
                {"amount": abs(amount),
                 "currency": input_currency}
            ,
            "output": data
        }
        return json.dumps(output, indent=4, sort_keys=True)
    else:
        return "Requested currency is not supported."


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Currency Converter', add_help=True)
    parser.add_argument('--amouth', action="store", type=float, dest="amount", required=True)
    parser.add_argument('--input_currency', action="store", dest="input_currency", required=True)
    parser.add_argument('--output_currency', action="store", dest="output_currency", default=None)
    parameters = parser.parse_args()
    print(currency_converter(parameters.amount, parameters.input_currency, parameters.output_currency))

