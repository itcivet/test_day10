from selenium.webdriver.support.wait import WebDriverWait


class BagePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element_funt(self, logcat, timeeou=5, poll=0.5):
        """元素定位方法"""
        element = WebDriverWait(self.driver, timeout=timeeou, poll_frequency=poll) \
            .until(lambda x: x.find_element(*logcat))
        return element

    def click_funt(self, location):
        """
        元素点击方法
        :param location: 元素定位信息
        :return:
        """
        element = self.find_element_funt(location)  # 元素定位
        element.click()  # 元素点击

    def input_funt(self, location, text):
        """
        元素输入方法
        :param location: 元素定位信息
        :param text:  输入信息
        :return:
        """
        element = self.find_element_funt(location)
        element.clear()  # 清空
        element.send_keys(text)  # 输入

    # def click_funt(self, element):
    #     """元素点击方法"""
    #     element.click()

    # def input_funt(self, element, text):
    #     """元素输入方法"""
    #     element.clear()
    #     element.send_keys(text)
