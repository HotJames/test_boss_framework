import time
import os
import shelve
from logs import logger
from selenium.webdriver.support.wait import WebDriverWait

logger = logger.Logger(logger_name='root').getlogger()


class BasePage(object):
    '''
    测试类继承该类
    封装常用的方法
    '''

    def __init__(self, driver):
        self.driver = driver

    # 打开对应URL浏览器
    def open_browser(self, url):
        self.driver.get(url)
        time.sleep(2)

    def close_browser(self):
        self.driver.close()

    # 显性等待，设置了默认超时时间和检查时间间隔
    def domi_wait(self, max_second=20, check_second=0.7):
        wait = WebDriverWait(self.driver, max_second, check_second)
        return wait

    # 退出浏览器结束测试
    def quit_browser(self):
        self.driver.quit()

    # 关闭当前窗口
    def close(self):
        try:
            self.driver.close()
        except NameError as e:
            logger.error("Failed to quit the browser with %s" % e)

    # 写入一条数据用于交互
    def write_json(self, key, value):
        file_path = os.path.dirname(os.path.abspath('.')) + '/tempdict/tempjson'
        f = shelve.open(file_path)
        f[key] = value
        f.close()

    # 写入客户开户生成的数据以及开户成功后的流水号
    def write_temp(self, links, data_dict,):
        a, b = links.split('：')
        file_path = os.path.dirname(os.path.abspath('.')) + '/tempdict/tempjson'
        f = shelve.open(file_path)
        f['客户类别'] = data_dict['客户类别']
        f['客户级别'] = data_dict['客户级别']
        f['客户名称'] = data_dict['客户名称']
        f['证件类型'] = data_dict['证件类型']
        f['证件号码'] = data_dict['证件号码']
        f['联系人'] = data_dict['联系人']
        f['联系电话'] = data_dict['联系电话']
        f['邮政编码'] = data_dict['邮政编码']
        f['电子邮箱'] = data_dict['电子邮箱']
        f['一般纳税人'] = data_dict['一般纳税人']
        f['联系地址'] = data_dict['联系地址']
        f['受理流水号'] = b
        print('data_dict write to file')
        f.close()

    # 获得写入的数据
    def get_temp(self):
        data_dict = dict()
        file_path = os.path.dirname(os.path.abspath('.')) + '/tempdict/tempjson'
        f = shelve.open(file_path)
        data_dict['客户类别'] = f['客户类别']
        data_dict['客户级别'] = f['客户级别']
        data_dict['客户名称'] = f['客户名称']
        data_dict['证件类型'] = f['证件类型']
        data_dict['证件号码'] = f['证件号码']
        data_dict['联系人'] = f['联系人']
        data_dict['联系电话'] = f['联系电话']
        data_dict['邮政编码'] = f['邮政编码']
        data_dict['电子邮箱'] = f['电子邮箱']
        data_dict['一般纳税人'] = f['一般纳税人']
        data_dict['联系地址'] = f['联系地址']
        data_dict['受理流水号'] = f['受理流水号']
        f.close()
        return data_dict

    # 浏览器截图，可以在报错的时候使用
    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        print(screen_name)
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.error("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()


