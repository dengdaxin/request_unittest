# encoding:utf-8
# @author:ddx
# @time:2021/6/27 16:12
import json
import unittest
import jsonpath
import requests


class Demo(unittest.TestCase):

    def setUp(self) -> None:
        self.acctoken = ''
        self.session = requests.Session()

    def tearDown(self) -> None:
        self.session.close()

    def get_tokoen(self):
        kw = {'grant_type': 'client_credential',
              'appid': 'wx95b88e450068c8d2',
              'secret': '5b6d758ece15c636e2c0a16fe56a2d97'}
        res = requests.get('https://api.weixin.qq.com/cgi-bin/token', params=kw)
        token = jsonpath.jsonpath(res.json(), '$.access_token')[0]
        self.a = 1
        return token

    # def test_get_token(self):
    #     kw = {'grant_type': 'client_credential',
    #           'appid': 'wx95b88e450068c8d2',
    #           'secret': '5b6d758ece15c636e2c0a16fe56a2d97'}
    #     res = requests.get('https://api.weixin.qq.com/cgi-bin/token', params=kw)
    #     data = jsonpath.jsonpath(res.json(), '$.expires_in')[0]
    #     self.acctoken = jsonpath.jsonpath(res.json(), '$.access_token')
    #     self.assertEqual(data,7200,'test_get_token测试失败')

    def test_createtag(self):
        print(self.acctoken)
        self.token = {'access_token': self.get_tokoen()}
        tag_name = {"tag": {"name": "150KKk7892"}}
        host = 'https://api.weixin.qq.com/cgi-bin/tags/create'
        re = self.session.post(host, params=self.token, data=json.dumps(tag_name))  # json.dumps()把字典转换成json对象
        print(re.text)
        self.assertIn('id',re.text, 'test_createtag测试失败')


if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTest(Demo('test_createtag'))
    unittest.main(defaultTest='suite')