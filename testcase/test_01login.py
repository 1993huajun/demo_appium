# -- coding: utf-8 --
from common.myunit import StartEnd
from bussinessView.login.loginView import loginView
import unittest

class test_login(StartEnd):

    def test_01loginNormal(self):
        po = loginView(self.driver)
        po.type_loginNormal()
        print("先提交到dev，后与master合并.")

    # def test_02

if __name__ == '__main__':
    unittest.main()