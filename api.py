from flask import Flask, request
import currency_converter

app = Flask(__name__)


@app.route('/currency_converter', methods=['GET'])
def get():
    amount = request.args.get('amount', type=float)
    input_currency = request.args.get('input_currency')
    output_currency = request.args.get('output_currency', default=None)
    return currency_converter.currency_converter(amount, input_currency, output_currency)


if __name__ == '__main__':
    app.run()