import unittest
from currency_converter import currency_converter,get_rate,get_currency_code


class test_currency_converter(unittest.TestCase):

    def test_get_rate(self):
        self.assertEqual(get_rate('CZK','EUR'), get_rate('CZK','EUR'))
        self.assertEqual(get_rate('X',None),None)
        self.assertEqual(get_rate('EUR','X'),None)

    def test_get_currency_code(self):
        self.assertEqual(get_currency_code('$'),"USD")
        self.assertEqual(get_currency_code('X'),None)

    def test_currency_converter(self):
        self.assertEqual(currency_converter(10,'CZK','¥'),currency_converter(10,'CZK','¥'))
        self.assertEqual(currency_converter('x','CZK','¥'),"Amount parameter is't float or int.")
        self.assertEqual(currency_converter(10.0,'EUR','X'),currency_converter(10.0,'EUR','X'))
        self.assertEqual(currency_converter(10.0,'XXXX','EUR'),"Requested currency is not supported.")
        self.assertEqual(currency_converter(10.0, 'EUR', None), currency_converter(10.0, 'EUR', None))