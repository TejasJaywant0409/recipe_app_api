from django.test import SimpleTestCase
from newApp import calc


class CalcTest(SimpleTestCase):
    def test_calc(self):
        res = calc.add(2, 3)
        self.assertEqual(res, 5)
