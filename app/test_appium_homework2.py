
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestAdd:
    def setup_class(self):
        caps = {}
        caps['platformName'] = 'android'
        caps['deviceName'] = 'emulator-5554'
        caps['deviceVersion'] = '5.1.1'
        caps['appPackage'] = 'com.tencent.wework'
        caps['appActivity'] = 'com.tencent.wework.launch.WwMainActivity'
        caps['noReset'] = 'True'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self.driver.implicitly_wait(5)

    @pytest.fixture()
    def add_fixture(self):
        yield
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gpp").click()

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("username, gender, phonenum", [
        ("飞血001", "男", "13601010101"),
        ("飞血002", "女", "13601010102"),
        ("飞血003", "女", "13601010103")
    ])


    def test_addcontact(self, add_fixture, username, gender, phonenum):
        # 进入到 通讯录
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()

        # 滚动查找 添加成员
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable('
                                                               'new UiSelector().scrollable(true).instance(0))'
                                                               '.scrollIntoView(new UiSelector().text("添加成员")'
                                                               '.instance(0));').click()
        # 手动添加
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/c56").click()

        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '姓名')]/..//*[@resource-id='com.tencent.wework:id/ase']").send_keys(
            username)

        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@text='性别']/..//*[@resource-id='com.tencent.wework:id/at7']").click()
        # 选择性别
        if gender == '男':
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("男")').click()
        else:
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("女")').click()

        # 输入手机号
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/emh").send_keys(phonenum)

        # 点击 保存
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gq7").click()

        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")

    @pytest.mark.parametrize("username", [
        ("飞血001"),
        ("飞血002"),
        ("飞血003")
    ])

    def test_deletecontact(self, username):
        # 进入到 通讯录
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 点击要删除的用户
        self.driver.find_element_by_xpath(f'//*[@text="{username}"]').click()
        # 点击更多
        self.driver.find_element_by_id("com.tencent.wework:id/gq0").click()
        # 点击编辑成员
        self.driver.find_element_by_id("com.tencent.wework:id/axr").click()
        # 点击删除成员
        self.driver.find_element_by_id("com.tencent.wework:id/drk").click()
        # 点击确定
        self.driver.find_element_by_id("com.tencent.wework:id/b89").click()
        # 点击我
        self.driver.find_element_by_xpath('//*[@text="我"]').click()
        # 点击通讯录
        self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()

