# -- coding: utf-8 --
from baseView.baseView import BaseView
import os,logging,csv,time

class Common(BaseView):

    #屏幕截图
    def common_screenShot(self, module):
        time = self.common_getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (module, time)
        logging.info('get %s screenshot' % module)
        self.driver.get_screenshot_as_file(image_file)

    def common_getCsvData(self, csv_file, line):
        '''
        获取csv文件指定行的数据
        :param csv_file: csv文件路径
        :param line: 数据行数
        :return: 
        '''
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row

    def common_getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

