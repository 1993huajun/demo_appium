# -- coding: utf-8 --
from ruamel import yaml
import logging.config
from appium import webdriver
import os

CON_LOG = "../config/log.conf"
#通过解析conf配置文件实现
logging.config.fileConfig(CON_LOG)
''' 
指定name，返回一个名称为name的Logger实例。
如果再次使用相同的名字，是实例化一个对象。
未指定name，返回Logger实例，名称是root，即根Logger。
'''
logging = logging.getLogger()

def appium_desired():
    with open('../config/kyb_caps.yaml',mode='r',encoding='utf-8') as file:
        data = yaml.load(file,Loader=yaml.RoundTripLoader)

        desired_caps={}

        desired_caps['platformName']=data['platformName']#手机操作系统
        desired_caps['platformVersion'] = data['platformVersion']#系统版本
        desired_caps['deviceName'] = data['deviceName']#设备名称

        # 找到当前文件目录的上级目录，os.path.dirname(__file__)表示当前目录
        base_dir = os.path.dirname(os.path.dirname(__file__))
        app_path = os.path.join(base_dir, 'app', data['appname'])#找到测试APP的相对路径
        desired_caps['app'] = app_path

        # 不要在会话前重置应用状态，appium启动app时会自动清除app里面的数据。设置为TRUE可以不清除掉里面的数据。
        desired_caps['noReset'] = data['noReset']

        desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']##使用Unicode编码方式发送字符串
        desired_caps['resetKeyboard'] = data['resetKeyboard']#表示在测试结束后切回系统输入法。

        desired_caps['appPackage'] = data['appPackage']#找到package名，相当于身份证，是唯一的
        desired_caps['appActivity'] = data['appActivity']#找到启动的activity

        logging.info('start run app...')
        #传入配置信息，并用webdriver.Remote()启动APP
        driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
        driver.implicitly_wait(5)
        return driver

if __name__ == '__main__':
    appium_desired()


