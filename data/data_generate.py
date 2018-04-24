import random
import time
import string


class DataGenerate(object):

    '''
    客户开户测试数据的自动生成
    '''

    def __init__(self):
        # 客户类型
        self.customer_cate = ['企业', '个人']
        # 客户级别
        self.customer_lev = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # 证件类别
        self.cert_types = ['身份证', '企业营业执照号']
        # 是否一般纳税人
        self.gen_taxpayers = ['是', '否']
        # 邮箱后缀
        self.email_sufs = ['@163.com', '@qq.com', '@sina.com', '@sohu.com', '@yahoo.com']

        # 业务品牌

        #

    # 随机生成规则内数据
    def gene_data(self):
        # 随机客户类型
        cus_cate = random.sample(self.customer_cate, 1)[0]
        # 随机客户级别
        cus_lev = random.sample(self.customer_lev, 1)[0]
        # 时间戳加随机客户名称
        lt = time.localtime()
        lt2 = time.strftime('%y%m%d%H%M%S', lt)
        nl = []
        for i in range(0, random.randint(1, 8)):
            val = random.randint(0x4e00, 0x9fbf)
            nl.append(chr(val))
        nl2 = ''.join(nl)
        cus_name = nl2 + lt2
        # 随机证件类型
        cert_type = random.sample(self.cert_types, 1)[0]
        # 随机证件号码
        cert_num = random.randint(0, 100000000000000000000)
        # 随机联系人
        cnl = []
        for i in range(0, random.randint(1, 20)):
            val2 = random.randint(0x4e00, 0x9fbf)
            cnl.append(chr(val2))
        cnl2 = ''.join(cnl)
        # 随机联系电话
        con_tel = random.randint(0, 100000000000)
        # 随机邮政编码
        post_num = random.randint(0, 100000)
        # 随机邮箱
        src_digits = string.digits
        src_letter = string.ascii_lowercase
        email_sufs = ['@163.com', '@qq.com', '@sina.com', '@sohu.com', '@yahoo.com']
        num = random.randint(1, 30)
        digits_num = random.randint(1, num)
        letter_num = random.randint(0, (num - digits_num))
        email_num = []
        for i in range(digits_num):
            email_num += random.sample(src_digits, 1)[0]
        email_letter = []
        for i in range(letter_num):
            email_letter += random.sample(src_letter, 1)[0]
        email_pre = email_num + email_letter
        email_suf = random.sample(email_sufs, 1)[0]
        # 打乱字符串
        random.shuffle(email_pre)
        # 列表转字符串
        new_email_pre = ''.join(email_pre)
        email = new_email_pre + email_suf
        # 随机是否一般纳税人
        gen_taxpayer = random.sample(self.gen_taxpayers, 1)[0]
        # 随机联系地址
        addrl = []
        for i in range(0, random.randint(1, 100)):
            val3 = random.randint(0x4e00, 0x9fbf)
            addrl.append(chr(val3))
        address = ''.join(addrl)
        # 生成这条数据
        data = {
                   '客户类别': cus_cate,
                   '客户级别': cus_lev,
                   '客户名称': cus_name,
                   '证件类型': cert_type,
                   '证件号码': cert_num,
                   '联系人': cnl2,
                   '联系电话': con_tel,
                   '邮政编码': post_num,
                   '电子邮箱': email,
                   '一般纳税人': gen_taxpayer,
                   '联系地址': address
        }
        return data
