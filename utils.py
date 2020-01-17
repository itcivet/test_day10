from appium import webdriver


def ini_driver():
    capabilities = {
        "platformName": "Android",
        "platformVersion": "5.1",
        "deviceName": "模拟器",
        "appPackage": "com.bjcsxq.chat.carfriend",
        "appActivity": ".MainActivity",
        "resetKeyboard": True,  # 解决无法输入中文的问题
        "unicodeKeyboard": True
    }
    #com.bjcsxq.chat.carfriend/.MainActivity

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
    return driver

# def ini_driver():
#     capabilities = {
#         "platformName": "Android",
#         "platformVersion": "5.1",
#         "deviceName": "模拟器",
#         "appPackage": "com.bjcsxq.chat.carfriend",
#         "appActivity": ".MainActivity",
#         "resetKeyboard": True,  # 解决无法输入中文的问题
#         "unicodeKeyboard": True
#     }
#
#     driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
#     return driver


# 学车不 com.bjcsxq.chat.carfriend/.MainActivity
#
# if __name__ == '__main__':
#     ini_driver()
