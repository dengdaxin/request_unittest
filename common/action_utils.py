import unittest
import jsonpath
import requests
from common.config_utils import config
from common.basepage import BasePage

class ActionUtils(BasePage):
    #'''获取配送地址测试'''
    def get_addressList(self,host,params,data):
        response = self.session.post(host,params=params,data=data)
        return response


    def post(self,host,params,data):
        response = self.session.post(host,params=params,data=data)
        return response
