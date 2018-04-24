import os.path
from configparser import ConfigParser


class ConfParam(object):

    '''
    读取配置文件
    '''

    def __init__(self):
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        self.conf = ConfigParser()
        self.conf.read(file_path)

    @property
    def chrome_driver_path(self):
        driver_path = self.conf.get('browserDriverPath', 'driver_path1')
        return driver_path

    @property
    def firefox_driver_path(self):
        driver_path = self.conf.get('browserDriverPath', 'driver_path2')
        return driver_path

    @property
    def test_url1(self):
        url1 = self.conf.get('testServer', 'URL1')
        return url1

    @property
    def test_url2(self):
        url2 = self.conf.get('testServer', 'URL2')
        return url2

    @property
    def upload_file_path(self):
        file_path = self.conf.get('testFilePath', 'file_path').split('\n')
        return file_path


# a = ConfParam()
# print(a.chrome_driver_path)
# print(type(a.chrome_driver_path))