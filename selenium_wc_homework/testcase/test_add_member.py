from time import sleep

from selenium_wc_homework.page.index import Index


class TestAddMember:
    def setup(self):
        self.index = Index()
    def test_add_member(self):
        #goto add member实例化了AddMember
        add_member = self.index.goto_add_member()
        #添加成员
        add_member.add_member()
        sleep(2)
        #测试是否添加
        assert  add_member.get_first() == "taoataoatao"