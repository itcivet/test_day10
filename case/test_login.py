import time

import pytest

from page.page_factory import PageFactory
from read_data.read_yaml import build_login_data
from utils import ini_driver


class TestLogin(object):
    """登陆测试类"""

    @pytest.fixture(autouse=True)
    def befort_fun(self):
        """前置操作"""
        self.driver = ini_driver()  # 获取驱动对象
        self.page_factory = PageFactory(self.driver)
        yield
        time.sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize("num,pwd", build_login_data())
    def test_login(self, num, pwd):
        """测试登陆方法"""
        #
        # self.page_factory.index_page().click_mine()  # 点击我的
        # self.page_factory.mine_page().click_login_ret()  # 点击登录/注册
        # self.page_factory.login_page().input_phone_num("13580084109")  # 输入账号
        # self.page_factory.login_page().input_pwd("qiya77a369")  # 输入密码
        # self.page_factory.login_page().click_login_but()  # 点击登录
        # self.page_factory.login_page().click_alert_but()  # 点击弹出确认按钮

        self.page_factory.index_page().click_mine()  # 点击我的
        self.page_factory.mine_page().click_login_ret()  # 点击登录/注册
        self.page_factory.login_page().logint_func(num,pwd)  # 登陆操作
