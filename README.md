# currency_converter

Project contains API and CLI application of currency converter which convert 32 main world currencies.

## Prerequisites

* [flask 1.0.2] 
* [requests] 
* [argparse]  
* [json] 

## Installation
```sh
> pip install flask
> pip install requests 
...
```
### Setting flask

To run the appliaction, we have to complete a few things first. First, set the environment to development and tell your terminal the application to work with by exporting the FLASK_APP environment variable in Linux.
```sh
$ export FLASK_ENV=development
$ export FLASK_APP=api.py
```
and windows.

```sh
> set FLASK_ENV=development
> set FLASK_APP=api.py
```

### Run Flask

```sh
> flask run
```
or 
```sh
> py -m flask run
```
By default, the port is 5000`
* Running on http://127.0.0.1:5000

## How to use 
You can chose betwen CLI and API. Both has three arguments. Amount and input_currency, are required and output_currency, is optional. When output_currency is not fill currency conventer return conversion to all currencies. You can input three leter currency code (USD) or currency sign ($).
### CLI use example

```sh
./currency_converter.py --amount 100.0 --input_currency EUR --output_currency CZK
{   
    "input": {
        "amount": 100.0,
        "currency": "EUR"
    },
    "output": {
        "CZK": 2707.36, 
    }
}
```

or
```sh
./currency_converter.py --amount 10.92 --input_currency £ 
{
    "input": {
        "amount": 10.92,
        "currency": "GBP"
    },
    "output": {
        "EUR": 14.95,
        "USD": 17.05,
        "CZK": 404.82,
        .
        .
        .
    }
}
```

### API use example 
```sh
GET /currency_converter?amount=0.9&input_currency=¥&output_currency=AUD HTTP/1.1
{   
    "input": {
        "amount": 0.9,
        "currency": "CNY"
    },
    "output": {
        "AUD": 0.20, 
    }
}
```

or

```sh
GET /currency_converter?amount=10.92&input_currency=£ HTTP/1.1
{
    "input": {
        "amount": 10.92,
        "currency": "GBP"
    },
    "output": {
        "EUR": 14.95,
        "USD": 17.05,
        "CZK": 404.82,
        .
        .
        .
    }
}
```
