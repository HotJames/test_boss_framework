# from test_boss.customeraccount import CustomerAccount
from utils.base_page import BasePage
from selenium import webdriver
from data.conf_param import ConfParam
from test_boss_num import checkaccount_num as cn
from selenium.webdriver.support import expected_conditions as EC
from logs import logger
import time


logger = logger.Logger(logger_name='check_account').getlogger()


class CheckAccount(BasePage):
    '''
    测试按客户查询页面
    查询完成后校验
    '''
    def login(self):
        # self.driver.find_element(*cn.check_code_box).send_keys(1234)
        self.driver.find_element(*cn.login_button).click()
        time.sleep(3)

    def open_acc_page(self):
        wait.until(EC.presence_of_element_located(cn.che_cus_button))
        time.sleep(1)
        self.driver.find_element(*cn.che_cus_button).click()
        time.sleep(1)

    def search_name(self):
        wait.until(EC.presence_of_element_located(cn.search_button))
        self.driver.find_element(*cn.cus_name_box).send_keys(data_dict['客户名称'])
        self.driver.find_element(*cn.search_button).click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable(cn.open_info_button))
        self.driver.find_element(*cn.open_info_button).click()
        time.sleep(1)

    def check_data(self):
        wait.until(EC.presence_of_element_located(cn.cus_name))
        con_name = self.driver.find_element(*cn.con_name).text
        con_tel = self.driver.find_element(*cn.con_tel).text
        cert_type = self.driver.find_element(*cn.cert_type).text
        cert_num = self.driver.find_element(*cn.cert_num).text
        con_addr = self.driver.find_element(*cn.con_addr).text
        taxpayer = self.driver.find_element(*cn.taxpayer).text
        cus_id = self.driver.find_element(*cn.cus_id).text
        data = con_name.strip() +\
               con_tel.strip() + \
               cert_type.strip() + \
               cert_num.strip() + \
               con_addr.strip() + \
               taxpayer.strip()
        data_dict_new = str(data_dict['联系人']) + \
                        str(data_dict['联系电话']) + \
                        str(data_dict['证件类型']) + \
                        str(data_dict['证件号码']) + \
                        str(data_dict['联系地址']) + \
                        str(data_dict['一般纳税人'])
        if data == data_dict_new:
            print('校验一致')
            logger.info('校验一致')
        else:
            logger.error('校验不一致')
        return cus_id


CP = ConfParam()
driver = webdriver.Firefox(executable_path=CP.firefox_driver_path)
test = CheckAccount(driver)
test.open_browser(CP.test_url2)
wait = test.domi_wait()
data_dict = CheckAccount(driver).get_temp()
# print(data_dict)
try:
    test.login()
    test.open_acc_page()
    test.search_name()
    cus_id = test.check_data()
    test.write_json(key='客户编码', value=cus_id)
    test.close_browser()
except Exception as e:
    logger.error(e)
    test.get_windows_img()
    test.close_browser()