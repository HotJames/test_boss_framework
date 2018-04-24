import time
from utils.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from test_boss_num import customeraccount_num as cn
from data.conf_param import ConfParam
from data.data_generate import DataGenerate
from logs import logger


logger = logger.Logger(logger_name='customer_account').getlogger()


class CustomerAccount(BasePage):
    '''
    测试客户开户页面
    '''

    def login(self):
        # self.driver.find_element(*cn.check_code_box).send_keys(1234)
        self.driver.find_element(*cn.login_button).click()
        time.sleep(3)

    def open_acc_page(self):
        wait.until(EC.presence_of_element_located(cn.acc_button))
        self.driver.find_element(*cn.acc_button).click()

    def data_write(self):
        data_dict = DataGenerate().gene_data()
        wait.until(EC.presence_of_element_located(cn.submit_button))
        self.driver.find_element(*cn.cus_type_box).send_keys(data_dict['客户类别'])
        self.driver.find_element(*cn.cus_lev_box).send_keys(data_dict['客户级别'])
        self.driver.find_element(*cn.cus_name_box).send_keys(data_dict['客户名称'])
        self.driver.find_element(*cn.cert_type_box).send_keys(data_dict['证件类型'])
        self.driver.find_element(*cn.cert_num_box).send_keys(data_dict['证件号码'])
        self.driver.find_element(*cn.con_name_box).send_keys(data_dict['联系人'])
        self.driver.find_element(*cn.con_tel_box).send_keys(data_dict['联系电话'])
        self.driver.find_element(*cn.post_code_box).send_keys(data_dict['邮政编码'])
        self.driver.find_element(*cn.email_box).send_keys(data_dict['电子邮箱'])
        self.driver.find_element(*cn.con_addr_box).send_keys(data_dict['联系地址'])
        if data_dict['一般纳税人'] == '是':
            taxpayer_button = cn.taxpayer_y_button
        else:
            taxpayer_button = cn.taxpayer_n_button
        self.driver.find_element(*taxpayer_button).click()
        for i in CP.upload_file_path:
            self.driver.find_element(*cn.upload_file_box).send_keys(i)
        time.sleep(6)
        return data_dict

    def page_submit(self):
        wait.until(EC.element_to_be_clickable(cn.submit_button))
        self.driver.find_element(*cn.submit_button).click()
        wait.until(EC.element_to_be_clickable(cn.confirm_button))
        self.driver.find_element(*cn.confirm_button).click()

    def get_data(self):
        wait.until(EC.presence_of_element_located(cn.water_num))
        water_num = self.driver.find_element(*cn.water_num).text
        logger.info(water_num)
        print(water_num)
        return water_num


# if __name__ == '__main__':
CP = ConfParam()
driver = webdriver.Chrome(executable_path=CP.chrome_driver_path)
test = CustomerAccount(driver)
test.open_browser(CP.test_url1)
wait = test.domi_wait()
try:
    test.login()
    test.open_acc_page()
    data_dict = test.data_write()
    test.page_submit()
    links = test.get_data()
    test.write_temp(links, data_dict)
    time.sleep(1)
except Exception as e:
    test.get_windows_img()
    logger.error(e)
    test.quit_browser()
try:
    test.quit_browser()
except Exception as e:
    logger.error(e)
    time.sleep(2)
    test.quit_browser()
