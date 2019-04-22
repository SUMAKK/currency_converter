import flask
import currency_converter

app = flask.Flask(__name__)


@app.route('/currency_converter', methods=['GET'])
def get():
    amount = flask.request.args.get('amount', type=float)
    input_currency = flask.request.args.get('input_currency')
    output_currency = flask.request.args.get('output_currency', default=None)
    return currency_converter.currency_converter(amount, input_currency, output_currency)


if __name__ == '__main__':
    app.run()
