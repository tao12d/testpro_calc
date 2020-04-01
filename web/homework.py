import json
from time import sleep
from typing import List, Dict
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTest():
    def setup_method(self, method):
        chrome_opts=webdriver.ChromeOptions()
        chrome_opts.debugger_address="127.0.0.1:8888"
        self.driver = webdriver.Chrome(options=chrome_opts)
        self.driver.implicitly_wait(3)

    def teardown_method(self, method):
        self.driver.quit()

    def test_weixin(self):
        cookies = self.driver.get_cookies()

        with open("work_weixinregister_cookies", "w")as f:
            json.dump(cookies, f)

        with open("work_weixinregister_cookies", "r")as f:
            cookies: list[Dict] = json.load(f)


        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_item_title').click()


