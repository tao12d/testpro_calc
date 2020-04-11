from selenium.webdriver.common.by import By

from selenium_wc_homework.page.add_member import AddMember
from selenium_wc_homework.page.base_page import BasePage


class Index(BasePage):
    def goto_add_member(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap").click()
        # 对AddMember进行了实例化
        return AddMember(self.driver)
    def goto_import_address(self):
        pass
    def goto_member_join(self):
        pass