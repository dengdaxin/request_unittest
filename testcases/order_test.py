import HTMLTestRunner
import os
import time
import requests
import jsonpath
import unittest
from common.config_utils import config
from common.action_utils import ActionUtils
from common.unittest_utils import UnittestUtils

class RequestTest(UnittestUtils):

    def test_get_addressList(self):
        '''获取配送地址测试'''
        value = {'user_token':self.user_token}
        host = config.host_path + '/Jsonapi/addressList'
        addresslist = ActionUtils().get_addressList(host,params=self.apikey,data=value)
        msg = jsonpath.jsonpath(addresslist.json(),'$.msg')[0]
        self.assertEqual(msg,'信息调用成功！','test_get_addressList用例执行失败')

    def test_updata_address(self):
        '''添加或更新配送地址测试'''
        address_data = {'user_token':self.user_token, # 必填，用户登录唯一标识
                        'address_id':'',  # 非必填,为空时添加配送地址，不为空时更新配送地址
                        'true_name':'王八',   # 必填	收货人姓名
                        'region_id':'2504',   # 必填	最后选中的地区id，比如设置的北京市 朝阳区 那么region_id就是朝阳区的id
                        'region_value':'湖南省 常德市',# 必填	选中的所有地区的名称，比如设置的北京市 朝阳区 那么region_value就是 北京市 朝阳区
                        'address':'五一广场',     # 必填	详细地址
                        'zip_code':'100000',    # 必填	邮政编码
                        'mod_phone':'19944442222',   # 必填	手机号码
                        'tel_area_code':'',# 非必填 座机号码的区号
                        'tel_phone':'',   # 非必填 座机号码
                        'tel_ext':'',     # 非必填 座机分机号
                        'addr_default':''}# 非必填 是否为默认配送地址，1为默认配送地址
        updata_address = ActionUtils().post(config.host_path + '/Jsonapi/saveAddress',params=self.apikey,data=address_data)
        msg = jsonpath.jsonpath(updata_address.json(),'$.msg')[0]
        self.assertEqual(msg,'配送地址添加成功！','test_updata_address用例执行失败')

    def test_dle_address(self):
        '''删除配送地址测试'''
        del_address_data = {'user_token':self.user_token,'address_id':4}
        del_address = ActionUtils().post(config.host_path + '/Jsonapi/delAddress',params=self.apikey,data=del_address_data)
        msg = jsonpath.jsonpath(del_address.json(),'$.msg')[0]
        self.assertEqual(msg,'配送地址删除成功！','tesst_dle_address用例执行失败')

    def test_integralConvertMoney(self):
        '''积分转换金额测试'''
        data = {'user_token':self.user_token,
                'integral_num':100,         #  必填 积分数
                'cart_integral_num':5}    #  必填 本次购物可以使用多少积分购买
        Money = ActionUtils().post(config.host_path + '/Jsonapi/integralConvertMoney',params=self.apikey,data=data)
        status = jsonpath.jsonpath(Money.json(), '$.status')[0]
        self.assertEqual(status, 'success', 'test_integralConvertMoney用例执行失败')

    def test_get_regionlist(self):
        '''获取地区列表测试'''
        data = {'region_top_id':0} # 必填 上一级的地区id，0是获取顶级地区信息
        regionlist = ActionUtils().post(config.host_path + '/Jsonapi/region',params=self.apikey,data=data)
        msg = jsonpath.jsonpath(regionlist.json(), '$.msg')[0]
        self.assertEqual(msg, '信息调用成功！', 'test_get_regionlist用例执行失败')

    def test_step(self):
        '''购物车信息确认测试'''
        data = {'user_token':self.user_token,
                'address_id':1, # 非必填 配送地址id
                'user_unionid':self.user_unionid}
        step_info = ActionUtils().post(config.host_path + '/Jsonapi/step',params=self.apikey,data=data)
        msg = jsonpath.jsonpath(step_info.json(),'$.msg')[0]
        self.assertEqual(msg,'信息调用成功！','test_step用例执行失败')

    def test_cartSubmit(self):
        '''订单提交测试'''
        data = {'user_unionid':self.user_unionid,
                'address_id':1,                 # 必填	已经选择的配送地址id
                'user_token':self.user_token,
                'payment_code':'xxzf',               # 必填	支付方式标识码（支付方式里的 editaction 值）
                'express_id':7,                 # 必填	配送方式id
                'integral_buy_num':'',           # 非必填 用户使用的消费积分（只有购物车商品可以使用积分时，才会需要）
                'order_message':'',              # 非必填 订单留言信息
                'invoice_title':'',              # 非必填 发票抬头（文字形式）
                'invoice_content':'',            # 非必填 发票内容（文字形式）
                'shipping_time':'',              # 非必填 送货时间（文字形式）
                'coupon_id':''}                  # 非必填 当有可用优惠券，且选择了优惠券传过来的id值
        cartsubmit = ActionUtils().post(config.host_path + '/Jsonapi/cartSubmit',params=self.apikey,data=data)
        msg = jsonpath.jsonpath(cartsubmit.json(), '$.msg')[0]
        self.assertEqual(msg, '信息调用成功！', 'test_cartSubmit用例执行失败')
