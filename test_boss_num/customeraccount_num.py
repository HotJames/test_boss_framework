from selenium.webdriver.common.by import By


'''
客户开户事件数据
'''
# 验证码框
check_code_box = (By.ID, 'captcha')
# 登陆按钮
login_button = (By.ID, 'loginBtn')


# 客户开户按钮
acc_button = (By.XPATH, "//div[@id='bjui-sidenav-box']/ul/li/ul/li[5]/a")


# 客户类型
cus_type_box = (By.ID, 'cate')
# 客户级别
cus_lev_box = (By.NAME, 'level')
# 客户名称
cus_name_box = (By.ID, 'name')
# 证件类型
cert_type_box = (By.ID, 'type')
# 证件号码
cert_num_box = (By.NAME, 'clientNumber')
# 联系人
con_name_box = (By.NAME, 'contacts')
# 联系电话
con_tel_box = (By.NAME, 'tel')
# 邮政编码
post_code_box = (By.NAME, 'postCode')
# 电子邮箱
email_box = (By.NAME, 'email')
# 联系地址
con_addr_box = (By.NAME, 'addr')
# 一般纳税人是
taxpayer_y_button = (By.XPATH, "//input[@name='isTaxPayer']")
# 一般纳税人否
taxpayer_n_button = (By.XPATH, "(//input[@name='isTaxPayer'])[2]")
# 上传附件
upload_file_box = (By.NAME, 'file')


# 提交
submit_button = (By.ID, 'btn_client_submit')
# 确定提交
confirm_button = (By.CSS_SELECTOR, 'button.btn.btn-green')


# 流水号
water_num = (By.XPATH, '/html/body/div[10]/div[2]/div[2]/div[1]/div/div[2]/label')
