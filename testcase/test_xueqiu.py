import pytest
from page.Xueqiu import Xueqiu
from driver.Driver import Driver
import logging

class TestXueqiu(object):
    def setup(self):
        pass

    def test_xueqiu(self):
        xueqiu=Xueqiu()
        search=xueqiu.search("pdd")
        assert True==search.isInStock("拼多多")

    def test_search(self):
        assert True==Xueqiu().search("alibaba").isInStock("阿里巴巴")

    def test_search_error(self):
        assert False==Xueqiu().search("alibaba").isInStock("小米")


    def test_forget_password(self):
        assert "已发送" in Xueqiu().toLogin().findByEmail("1@qq.com")
    def teardown(self):
        Driver.quit()