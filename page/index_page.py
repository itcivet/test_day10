"""
首页页面
"""
import page
from Bage.Bage_page import BagePage


class IndexPage(BagePage):
    mine = page.mine

    def click_mine(self):
        """点击我的页面的方法"""
        self.click_funt(self.mine)
