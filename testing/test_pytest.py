from python.calc import Calc
import pytest


class TestCalc:
    def test_add1(self):
        calc = Calc()
        assert calc.add(1, 2) == 3

    def test_add3(self):
        calc = Calc()
        assert calc.add(1 / 2, 1 / 2) == 1

    def test_add4(self):
        calc = Calc()
        assert calc.add(1, 2) == 1

    def test_add2(self):
        calc = Calc()
        assert calc.add(0.1, 0.2) == 0.3
