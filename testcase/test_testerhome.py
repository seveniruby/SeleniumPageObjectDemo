import unittest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import pytest


class TestTesterHome(object):
    def test_testerhome(self):
        options = ChromeOptions()
        options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

        self.driver = webdriver.Chrome(
            executable_path="/Users/seveniruby/projects/chromedriver/72/chromedriver",
            options=options
        )

        self.driver.get("https://testerhome.com")

    @pytest.mark.parametrize("url",
                             [
                                 "https://testerhome.com",
                                 "https://testing-studio.com",
                                 "https://baidu.com"
                             ]
                             )
    def test_remote(self, url):
        options = webdriver.ChromeOptions()
        options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        print(options.to_capabilities())
        options.capabilities["platform"] = "MAC"

        driver = webdriver.Remote(
            "http://192.168.0.100:4444/wd/hub",
            desired_capabilities=options.to_capabilities(),
        )
        driver.get(url)



