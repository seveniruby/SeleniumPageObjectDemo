from pypom import Page
from selenium.webdriver.common.by import By
from driver.Driver import Driver
from time import sleep


class Login(Page):
    _forget=(By.XPATH, "//*[text()='忘记密码']")
    def __init__(self):
        super(Login, self).__init__(Driver.driver())

    def findByPhone(self):
        pass

    def findByEmail(self, mail):
        self.find_element(* self._forget).click()
        self.find_element(By.ID, "show_email_module").click()
        self.find_element(By.ID, "account_email").send_keys(mail)
        self.find_element(By.CSS_SELECTOR, ".email_next").click()
        element=self.find_element(By.CSS_SELECTOR, ".send_email .bottom_tip")
        self.wait.until(lambda s: element.text!="")
        print(element.text)


        return element.text


