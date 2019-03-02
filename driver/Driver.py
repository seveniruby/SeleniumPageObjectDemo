from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

class Driver(object):
    _driver=None
    @classmethod
    def driver(cls):
        if cls._driver==None:
            cls.initDriver()
        return cls._driver

    @classmethod
    def initDriver(cls):
        options = ChromeOptions()
        options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

        cls._driver=Chrome(
            executable_path="/Users/seveniruby/projects/chromedriver/72/chromedriver",
            options=options
        )
        cls._driver.implicitly_wait(10)

    @classmethod
    def quit(cls):
        if cls._driver!=None:
            cls._driver.quit()
            cls._driver=None