from baseView.baseView import BaseView
from common.common_fun import Common
from common.desired_caps import appium_desird
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
import time
import json
import requests
from businessView.loginView import  LoginView

class SwipeView(BaseView):
    #元素
    photos_list = (By.ID, 'com.guagua.marslive:id/rl_item')

    def swipetest(self):
        self.driver.find_elements(*self.photos_list)[0].click()
        time.sleep(2)
        for i in range(100):
            try:
                self.swipe(411,1100,411,150,1000)
                time.sleep(2)
                print(i)
            except:
                print("滑动异常")



if __name__=='__main__':
    driver = appium_desird()
    l = LoginView(driver)
    l.login_action('user')
    s = SwipeView(driver)
    s.swipetest()