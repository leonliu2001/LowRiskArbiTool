# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 11:24:57 2022
@author: Administrator
"""
import requests


class SinaTick:
    def __init__(self, code_no: str):
        self.code_no = code_no

    def get_stock(self):
        # 取股票当前数据
        url = "http://hq.sinajs.cn/list=" + self.code_no
        headers = {'referer': 'https://finance.sina.com.cn/'}
        page = requests.get(url, headers=headers)
        stock_info = page.text
        stock_data = stock_info[13:-3].replace('="', ',').split(',')
        return tick_data

    def get_opti(self):
        # 取股指期权当前数据
        url = "https://hq.sinajs.cn/etag.php?list=" + self.code_no
        headers = {'referer': 'https://finance.sina.com.cn/'}
        page = requests.get(url, headers=headers)
        option_info = page.text
        opti_data = option_info[13:-3].replace('="', ',').split(',')
        return opti_data

    def get_etf_opti(self):
        # 取etf期权当前数据
        url = "http://hq.sinajs.cn/list=" + self.code_no
        headers = {'referer': 'https://finance.sina.com.cn/'}
        page = requests.get(url, headers=headers)
        etf_option_info = page.text
        etf_opti_data = option_info[13:-3].replace('="', ',').split(',')
        return etf_opti_data
