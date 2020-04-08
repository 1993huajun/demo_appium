# -- coding: utf-8 --
from common.desired_caps import appium_desired
from common.common_fun import Common
from selenium.webdriver.common.by import By
from time import sleep

class loginView(Common):
    loginBtn_loc = (By.ID,"com.tencent.mm:id/d1w")
    accountLink_loc = (By.ID,"com.tencent.mm:id/bwm")
    account_loc = (By.ID,"com.tencent.mm:id/hx")
    password_loc = (By.XPATH,"//*[@id='com.tencent.mm:id/li' and @text='请填写密码']")
    submit_loc = (By.ID,"com.tencent.mm:id/cvg")

    def type_loginNormal(self):
        try:
            print("type_loginNormal")
            sleep(2)
            self.driver.find_element(*self.loginBtn_loc).click()
            sleep(2)
            self.driver.find_element(*self.accountLink_loc).click()

            self.driver.find_element(*self.account_loc).send_keys("***")
            self.driver.find_element(*self.password_loc).send_keys("***")
            self.driver.find_element(*self.submit_loc).click()
        except BaseException as msg:
            print(msg)


