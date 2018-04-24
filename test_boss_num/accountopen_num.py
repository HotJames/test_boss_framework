from selenium.webdriver.common.by import By


# 点击登陆

# 打开账户开户
open_page_button = (By.XPATH, "//div[@id='bjui-sidenav-box']/ul/li/ul/li[6]/a")
# 输入客户编码
search_code_box = (By.ID, 'searchCode')
# 查找按钮
search_button = (By.ID, 'btn_client_Search')


# 账户名称
acc_name_box = (By.ID, 'accountName')
# 业务品牌
bus_brand = (By.ID, 'brandCode')
# 开票名称
invoice_title = (By.NAME, 'invoiceTitle')
# 票据类型
invoice_type = (By.ID, 'invoiceType')
# 付费方式
pay_type = (By.ID, 'payType')
# 开户银行
acc_bank = (By.ID, 'bank')
# 银行账号
bank_num = (By.ID, 'bankAccount')