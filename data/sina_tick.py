# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 11:24:57 2022
@author: Administrator
"""
# 从新浪财经接口提取股票、转债（视同股票）、商品期货、股指期权、etf期权的实时数据，返回值为list。
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
        return stock_data

    def get_opti(self):
        # 取股指期权当前数据
        url = "https://hq.sinajs.cn/etag.php?list=" + self.code_no
        headers = {'referer': 'https://finance.sina.com.cn/'}
        page = requests.get(url, headers=headers)
        option_info = page.text
        opti_data = option_info[13:-3].replace('="', ',').split(',')
        return opti_data


    def get_cff_future(self):
        # 取中金所期货当前数据，代码格式如IC2207
        url = "http://hq.sinajs.cn/list=CFF_RE_" + self.code_no
        headers = {'referer': 'https://finance.sina.com.cn/'}
        page = requests.get(url, headers=headers)
        future_info = page.text
        future_data = future_info[18:-3].replace('="', ',').split(',')
        return future_data

    def get_merch_future(self):
        # 取商品期货当前数据，代码格式如M2207
        url = "http://hq.sinajs.cn/list=" + self.code_no
        headers = {'referer': 'https://finance.sina.com.cn/'}
        page = requests.get(url, headers=headers)
        merch_info = page.text
        merch_data = merch_info[15:-3].replace('="', ',').split(',')
        return merch_data


    def get_etf_opti(self):
        # 取etf期权当前数据，代码格式如10003707，为上交所公布的合约编号
        url = "http://hq.sinajs.cn/list=CON_SO_" + self.code_no
        headers = {'referer': 'https://finance.sina.com.cn/'}
        page = requests.get(url, headers=headers)
        etf_option_info = page.text
        etf_opti_data = etf_option_info[13:-3].replace('="', ',').split(',')
        return etf_opti_data
    
    def get_fund_nv(self):
        url = "https://stock.finance.sina.com.cn/fundInfo/api/openapi.php/CaihuiFundInfoService.getNav?symbol=" + self.code_no
        data = []
        # get netvalue of 511880 from sina
        html = requests.get(url).content
        # detect html code pattern
        encode_type = chardet.detect(html)
        html = html.decode(encode_type['encoding'])
        # divide string to List
        data = data + re.findall(u'\{"fbrq.*?"\}', html)
        # Transform Data to pandas
        Time = [''] * len(data)
        JJJZ = [''] * len(data)
        LJJZ = [''] * len(data)
        for k in range(len(data)):
            dataArray = data[k].split('"')
            Time[k] = pd.to_datetime(dataArray[3][0:10])
            JJJZ[k] = float(dataArray[7][0:10])
            LJJZ[k] = float(dataArray[11][0:10])
        df = pd.DataFrame({'Time': Time,
                           'JJJZ': JJJZ,
                           'LJJZ': LJJZ})
        df = df.drop_duplicates()
        df = df.sort_values(by='Time')
        df.index = range(len(df))
        return df
