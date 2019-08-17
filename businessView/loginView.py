from baseView.baseView import BaseView
from common.common_fun import Common
from common.desired_caps import appium_desird
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
import time
import json
import requests

class LoginView(BaseView):
    # 选择手机号登录
    phone_login = (By.ID, 'lb_phone')
    google_login = (By.ID, 'lb_google')
    twitter_login = (By.ID, 'lb_twitter')
    # 登录元素
    btn_login_phone = (By.ID, 'com.guagua.marslive:id/btn_login')
    btn_login_auth = (By.ID, 'com.guagua.marslive:id/tv_authorize')
    home_btn = (By.ID, 'com.guagua.live.testint:id/rb_live')

    def login_action(self, username):
        time.sleep(10)
        logging.info('=======login action====')
        time.sleep(1)


        # 点击登录按钮
        self.driver.find_element(*self.btn_login_phone).click()
        self.driver.implicitly_wait(2)

        logging.info('=======login finshed====')

        try:
            element = self.driver.find_element(*self.home_btn)
        except NoSuchElementException:
            logging.info("fail")
        else:
            element.click()
            logging.info("sucess")


if __name__ == '__main__':

    driver = appium_desird()
    l = LoginView(driver)
    l.login_action('17600629988')
    time.sleep(5)
    # module = 'phone_login'
    common = Common(driver)
    common.getScreenShot('login')