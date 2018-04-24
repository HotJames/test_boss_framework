import logging
import os.path
import time


class Logger(object):
    '''
        指定日志路径，级别
        两个具柄，一个信息和错误写入，一个单独写入错误
        getlogger()返回实例对象
    '''

    def __init__(self, logger_name):

        # 需要一个一个传参，不传为root，生成实例对象
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO)

        # 时间字符串
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # 日志路径
        log_path = os.path.dirname(os.path.abspath('.')) + '/logs/logfiles/'
        # 拼接路径和日志文件名
        log_name1 = log_path + rq + '.log'
        log_name2 = log_path + rq + 'error.log'

        # 两个具柄一个写入详细，一个只写入信息
        fh1 = logging.FileHandler(log_name1)
        fh1.setLevel(logging.INFO)
        fh2 = logging.FileHandler(log_name2)
        fh2.setLevel(logging.ERROR)

        # 定义日志记录格式
        formatter = logging.Formatter('%(name)s %(asctime)s : %(levelname)s %(message)s')
        fh1.setFormatter(formatter)
        fh2.setFormatter(formatter)

        # 给logger添加handle
        self.logger.addHandler(fh1)
        self.logger.addHandler(fh2)

    # 返回实例对象
    def getlogger(self):
        return self.logger