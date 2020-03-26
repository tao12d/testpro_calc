from python.calc import Calc
import pytest


class TestCalc:
    def setup(self):
        self.calc = Calc()

    def test_add1(self):
        assert self.calc.add(1, 2) == 3

    def test_add2(self):
        assert self.calc.add(1 / 2, 1 / 2) == 1

    def test_add3(self):
        assert self.calc.add(1, 2) != 1

    def test_add4(self):
        assert self.calc.add(0.01, 0.02) == 0.03

    def test_div1(self):
        assert self.calc.div(4, 2) == 2

    def test_div2(self):
        assert self.calc.div(2, 4) == 0.5

    def test_div3(self):
        assert self.calc.div(0, 2) == 0

    def test_div4(self):
        assert self.calc.div(4, 3) != 3

    def test_div5(self):
        assert self.calc.div(4, 3) != 3

    def test_div5(self):
        assert self.calc.div(2, 0) == "ZeroDivisionError: division by zero"
