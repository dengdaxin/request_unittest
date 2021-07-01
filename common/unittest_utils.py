import unittest
import warnings
import jsonpath
import requests
from common.config_utils import config


class UnittestUtils(unittest.TestCase):
    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)   # 解决警告信息
        self.session = requests.session()
        self.apikey = {'apikey': config.apikey}
        key = {'user_name': 'ddx01', 'user_password': '123456', 'user_unionid': ''}
        login = requests.post(config.host_path + '/Jsonapi/login', params=self.apikey, data=key)
        self.user_token = jsonpath.jsonpath(login.json(), '$..user_token')[0]
        self.user_unionid = jsonpath.jsonpath(login.json(), '$..user_unionid')[0]

    def tearDown(self) -> None:
        self.session.close()


