"""
统一入口类====工厂方法
"""
from page.index_page import IndexPage
from page.login_page import LoginPage
from page.mine_page import MinePage


class PageFactory(object):
    def __init__(self, driver):
        self.driver = driver

    def index_page(self):
        """首页页面"""
        return IndexPage(self.driver)

    def mine_page(self):
        """我的页面"""
        return MinePage(self.driver)

    def login_page(self):
        """登陆页面"""
        return LoginPage(self.driver)
