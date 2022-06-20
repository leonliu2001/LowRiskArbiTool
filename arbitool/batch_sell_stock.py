# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 16:12:55 2022

@author: Leonliu2001
"""


import pandas as pd
import time
from sina_tick import SinaTick
from THS.THSTrader import THSTrader


def batch_sell_stock():

    stock_codes = pd.read_csv('../csv/cbold.csv', header=None, index_col=0, squeeze=True).to_dict()
    # 从csv文件读取转债的代码和名称，文件中的转债为当前持有的
    stock_keys = list(cbond_codes.keys())  # 取代码为List
    for stock_key in stock_keys:
        if str(stock_key).startswith('11'):  # 挑选上海交易所的转债
            stock_no_sh = 'sh' + str(stock_key)    # 增加sh标识
            stock_ticks_sh = SinaTick(stock_no_sh)
            stock_tick_sh = stock_ticks_sh.get_stock()  #  抽取股票当前价格
            sell_price_sh = float(stock_tick_sh[3])+3
            print(stock_tick_sh[3])
            trader_sh = THSTrader(r"C:\同花顺\xiadan.exe")  # 连接同花顺下单的客户端
            result_sh = trader_sh.sell(stock_no=stock_key, amount=20, price=str(sell_price_sh))
            print(result_sh)
            time.sleep(5)
        if str(stock_key).startswith('12'):  # 挑选深圳交易所的转债
            stock_no_sz = 'sz' + str(stock_key)    # 增加sz标识
            stock_ticks_sz = SinaTick(stock_no_sz)
            stock_tick_sz = stock_ticks_sz.get_stock()
            sell_price_sz = float(stock_tick_sz[3])+3
            print(stock_tick_sz[3])
            trader_sz = THSTrader(r"C:\同花顺\xiadan.exe")  # 连接同花顺下单的客户端，调用Tu5039的THS库
            result_sz = trader_sz.sell(stock_no=stock_key, amount=20, price=str(sell_price_sz))
            print(result_sz)
            time.sleep(5)

if __name__ == "__main__":
    batch_sell_stock()
