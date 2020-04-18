from time import sleep
import pytest
from appium import webdriver


class TestWe_work():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'android'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['deviceVersion'] = '5.1.1'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = 'com.tencent.wework.launch.WwMainActivity'
        desired_caps['noReset'] = 'True'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        #self.driver.quit()
        el8 = self.driver.find_element_by_id("com.tencent.wework:id/gpp")
        el8.click()

    def test_search(self):
        el1 = self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/dnj' and @text='通讯录']")
        #el1 = self.driver.find_element_by_xpath(
            #"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.View/android.widget.RelativeLayout[2]/android.widget.TextView")
        el1.click()
        el2 = self.driver.find_element_by_id("com.tencent.wework:id/gq_")
        el2.click()
        el3 = self.driver.find_element_by_id("com.tencent.wework:id/ffq")
        el3.send_keys("是")
        el4 = self.driver.find_element_by_id("com.tencent.wework:id/czs")
        el4.click()
        el5 = self.driver.find_element_by_id("com.tencent.wework:id/aaj")
        el5.click()
        el6 = self.driver.find_element_by_id("com.tencent.wework:id/dtv")
        el6.send_keys("测试code")
        el7 = self.driver.find_element_by_id("com.tencent.wework:id/dtr")
        el7.click()
        sleep(2)
