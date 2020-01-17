"""
登陆页面
"""
import page
from Bage.Bage_page import BagePage


class LoginPage(BagePage):
    phone_num = page.phone_num
    pwd = page.pwd
    login_but = page.logint_but
    alert_but = page.alert_but

    def input_phone_num(self, num):
        """输入手机号码方法"""
        self.input_funt(self.phone_num, num)

    def input_pwd(self, pwd):
        """输入密码方法"""
        self.input_funt(self.pwd, pwd)

    def click_login_but(self):
        """点击登录按钮方法"""
        self.click_funt(self.login_but)

    def click_alert_but(self):
        """点击弹出框确认按钮方法"""
        self.click_funt(self.alert_but)
    def logint_func(self,num,pwd):
        """登陆操作方法"""
        self.input_phone_num(num)
        self.input_pwd(pwd)
        self.click_login_but()
        self.click_alert_but()