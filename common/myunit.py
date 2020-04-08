# -- coding: utf-8 --
import unittest
from common.desired_caps import appium_desired
import logging
from time import sleep

class StartEnd(unittest.TestCase):
    driver = appium_desired()

    @classmethod
    def setUpClass(cls):
        logging.info('======setUp=========')
        cls.driver.implicitly_wait(6)

    @classmethod
    def tearDownClass(cls):
        logging.info('======tearDown=====')
        sleep(5)
        cls.driver.close_app()

