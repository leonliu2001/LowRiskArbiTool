# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 16:12:55 2022

@author: Leonliu2001
"""


import pandas as pd
from sina_tick import SinaTick
from send_wechat import SendWechat


def cbond_price_mon():
    cbond_codes = pd.read_csv('../csv/cbond.csv', header=None, index_col=0, squeeze=True).to_dict()
    # 从csv文件读取转债的代码和名称，cbond.csv格式见文件
    cbond_keys = list(cbond_codes.keys())  # 取代码为List
    mon_ratio = 0.05  # 监控的阈值，可根据需要调整阈值
    for cbond_key in cbond_keys:
        if str(cbond_key).startswith('11'):  # 挑选上海交易所的转债
            cbond_no_sh = 'sh' + str(cbond_key)    # 增加sh标识
            cbond_ticks_sh = SinaTick(cbond_no_sh)
            cbond_tick_sh = cbond_ticks_sh.get_stock() #取实时报价
            change_ratio = (float(cbond_tick_sh[4]) - float(cbond_tick_sh[3])) / float(cbond_tick_sh[3])
            if change_ratio >= mon_ratio:
                print(change_ratio) 
                send_msg = SendWechat("较昨日上涨"+str(change_ratio), "xx@163.com", cbond_tick_sh[1], "xx@qq.com", "smtp发送密钥")
                #  xx@163.com，xx@qq.com请用本人邮箱替换，smtp发送密钥用本人邮箱的发送密钥
                send_msg.send_wechat()
        if str(cbond_key).startswith('12'):  # 挑选深圳交易所的转债
            cbond_no_sz = 'sz' + str(cbond_key)    # 增加sz标识
            cbond_ticks_sz = SinaTick(cbond_no_sz)
            cbond_tick_sz = cbond_ticks_sz.get_stock()
            change_ratio = (float(cbond_tick_sz[4]) - float(cbond_tick_sz[3])) / float(cbond_tick_sz[3])
            if change_ratio >= mon_ratio:
                print(change_ratio)
                send_msg = SendWechat("较昨日上涨" + str(change_ratio), "xx@163.com", cbond_tick_sz[1], "xx@qq.com", "smtp发送密钥")
                send_msg.send_wechat()


if __name__ == "__main__":
    cbond_price_mon()
