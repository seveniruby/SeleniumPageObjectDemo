from pypom import Page
from selenium.webdriver.common.by import By
from driver.Driver import Driver
from time import sleep

class Search(Page):
    _stock=(By.XPATH, "//*[@class='search__tabs__border']//*[text()='股票']")
    _all=(By.XPATH, "//*[@class='search__tabs__border']//*[text()='综合']")

    def __init__(self):
        super(Search, self).__init__(Driver.driver())

    @property
    def loaded(self):
        self.seed_url="https://xueqiu.com/k"
        return self.seed_url in self.driver.current_url

    def isInStock(self, keyword):
        self.find_element(* self._stock).click()
        x=(By.XPATH, "//table//*[text()='" + keyword + "']")
        return self.is_element_displayed(*x)
