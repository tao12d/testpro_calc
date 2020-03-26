from python.calc import Calc
import pytest


class TestCalc:
    def setup(self):
        self.calc = Calc()

    # 正常的加法
    def test_add1(self):
        assert self.calc.add(1, 2) == 3

    # 分数的加法
    def test_add2(self):
        assert self.calc.add(1 / 2, 1 / 2) == 1

    # 错误的加法
    def test_add3(self):
        assert self.calc.add(1, 2) != 1

    # 小数点的加法
    def test_add4(self):
        assert self.calc.add(0.01, 0.02) == 0.03

    # 负数的加法
    def test_add5(self):
        assert self.calc.add(-1, -2) == -3

    # 包含0的加法
    def test_add6(self):
        assert self.calc.add(0, 2) == 2

    # 2个0的加法
    def test_add7(self):
        assert self.calc.add(0, 0) == 0

    # 正常的除法
    def test_div1(self):
        assert self.calc.div(4, 2) == 2

    # 除法答案中包含小数点
    def test_div2(self):
        assert self.calc.div(2, 4) == 0.5

    # 除法过程中包含小数点
    def test_div3(self):
        assert self.calc.div(0.4, 0.2) == 2

    # 除法第一个数字为0
    def test_div4(self):
        assert self.calc.div(0, 2) == 0

    # 错误的除法为0
    def test_div5(self):
        assert self.calc.div(4, 3) != 3

    # 除法中包含负数
    def test_div6(self):
        assert self.calc.div(-4, 2) == -2

    # 除法中不能被整除
    def test_div7(self):
        assert self.calc.div(5, 3) != 1.666

    # 除法中第二位数不能为0
    def test_div8(self):
        try:
            self.calc.div(3, 0)
        except Exception as error:
            print(error)
