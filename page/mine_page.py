"""
我的页面
"""
import page
from Bage.Bage_page import BagePage


class MinePage(BagePage):
    login_ret = page.login_ret

    def click_login_ret(self):
        """点击登录/注册页面方法"""
        self.click_funt(self.login_ret)
