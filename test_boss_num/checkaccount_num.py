from selenium.webdriver.common.by import By


'''
按客户查询事件数据
'''

# 登陆按钮
login_button = (By.ID, 'loginBtn')


# 按客户查询页面
che_cus_button = (By.XPATH, "//div[@id='bjui-sidenav-box']/ul/li/ul/li[4]/a")
# 客户名称输入框
cus_name_box = (By.NAME, 'clientName')

# 查询按钮
search_button = (By.ID, 'btn_client_Search')
# 打开详细信息
open_info_button = (By.XPATH, "//table[@id='mmg']/tbody/tr/td/span/input")


# 客户名称
cus_name = (By.XPATH, '//*[@id="name"]')
# 客户编码
cus_id = (By.XPATH, '//*[@id="code"]')
# 联系人
con_name = (By.XPATH, '//*[@id="contacts"]')
# 联系电话
con_tel = (By.XPATH, '//*[@id="tel"]')
# 证件类型
cert_type = (By.XPATH, '//*[@id="typeName"]')
# 证件号码
cert_num = (By.XPATH, '//*[@id="clientNumber"]')
# 联系地址
con_addr = (By.XPATH, '//*[@id="addr"]')
# 一般纳税人
taxpayer = (By.XPATH, '//*[@id="isTaxPayerName"]')