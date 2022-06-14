# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 09:18:10 2021

@author: leonliu2001
"""

import json
import re
import requests

'''
通过基金编码获取估值,返回字典格式，字典内容有：
基金代码fund_code,基金名称name,净值日期jzrq,单位净值dwjz,估算值gsz,估算值增量gszzl,估算时间gztime
'''


class TtjjData:

    def __init__(self, fund_code: str):
        self.fund_code = fund_code

    def get_nv(self):
        url = 'http://fundgz.1234567.com.cn/js/%s.js' % self.fund_code
        result = requests.get(url)  # 发送请求
        data = json.loads(re.match(".*?({.*}).*", result.text, re.S).group(1))
        return data
