from python.calc import Calc
import pytest


class TestCalc:
    def test_add1(self):
        calc = Calc()
        assert calc.add(1, 2) == 3

    def test_add2(self):
        calc = Calc()
        assert calc.add(1/2, 1/2) == 1

    def test_add3(self):
        calc = Calc()
        assert calc.add(1, 2) != 1

    def test_add4(self):
        calc = Calc()
        assert calc.add(0.01, 0.02) == 0.03

    def test_div1(self):
        calc = Calc()
        assert calc.div(4, 2) == 2

    def test_div2(self):
        calc = Calc()
        assert calc.div(2, 4) == 0.5

    def test_div3(self):
        calc = Calc()
        assert calc.div(0, 2) == 0

    def test_div4(self):
        calc = Calc()
        assert calc.div(4, 3) != 3

    def test_div5(self):
        calc = Calc()
        assert calc.div(4, 3) != 3

    def test_div5(self):
        calc = Calc()
        assert calc.div(2, 0) == "ZeroDivisionError: division by zero"