
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import unittest
from time import sleep


class TestKe(unittest.TestCase):
    def test_sort(self):
        options = ChromeOptions()
        #options.binary_location="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        #options.add_argument("user-data-dir=/Users/seveniruby/Library/Application Support/Google/Chrome/")
        #options.add_experimental_option("user-data-dir", "/Users/seveniruby/Library/Application Support/Google/Chrome/Default/")
        options.debugger_address = "127.0.0.1:" + '9222'
        browser = webdriver.Chrome(
            executable_path="/Users/seveniruby/projects/chromedriver/72/chromedriver",
            options=options)
        browser.get("https://ke.qq.com")
        #browser.find_element_by_xpath("//*[text]")
        sleep(10)

