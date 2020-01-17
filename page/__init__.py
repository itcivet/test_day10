from selenium.webdriver.common.by import By

# 首页页面
mine = By.XPATH, "//*[contains(@text,'我的')]"  # 我的

# 我的页面
login_ret = By.XPATH, "//*[contains(@text,'登录')]"  # 登陆/注册

# 登录页面
phone_num = By.ID, "com.bjcsxq.chat.carfriend:id/login_phone_et"  # 账号
pwd = By.ID, "com.bjcsxq.chat.carfriend:id/login_pwd_et"  # 密码
logint_but = By.ID, "com.bjcsxq.chat.carfriend:id/login_btn"  # 点击登录
alert_but = By.ID, "com.bjcsxq.chat.carfriend:id/btn_neg"  # 弹出确认框
