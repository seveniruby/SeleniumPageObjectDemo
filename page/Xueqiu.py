from pypom import Page
from selenium.webdriver.common.by import By
from driver.Driver import Driver
from page.Search import Search
from page.Login import Login


class Xueqiu(Page):
    _q=(By.NAME , "q")
    _login=(By.XPATH, "//*[text()='登录']")

    def __init__(self):
        super(Xueqiu, self).__init__(Driver.driver(), "https://xueqiu.com")
        self.open()

    @property
    def loaded(self):
        return self.seed_url in self.driver.current_url

    def search(self, keyword):
        self.find_element(*self._q).send_keys(keyword)
        self.find_element(By.CSS_SELECTOR, ".nav__search").submit()
        return Search()



    def getName(self):
        self.find_element(By.CSS_SELECTOR, ".search__tabs__border > a[href='#/stock']").click()
        text = self.find_element(By.CSS_SELECTOR, ".search__stock__bd__code").text
        return text


    def toLogin(self):
        self.find_element(* self._login).click()
        return Login()
