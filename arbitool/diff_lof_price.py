# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 16:12:55 2022

@author: Leonliu2001
"""


import pandas as pd
from sina_tick import SinaTick
from ttjj_data import TtjjData


def diff_lof_price():
    lof_codes = pd.read_csv('../csv/lof.csv', header=None, index_col=0, squeeze=True).to_dict()
    # 从csv文件读取lof的代码和名称
    lof_keys = list(lof_codes.keys())  # 取代码为List
    for lof_key in lof_keys:
        lof_no = 'sz' + str(lof_key)    # 增加sz标识
        lof_ticks = SinaTick(lof_no)
        lof_tick = lof_ticks.get_stock()
        print(str(lof_key))
        print("现价", lof_tick[4])
        lof_esti_values = TtjjData(str(lof_key))
        lof_esti_value = lof_esti_values.get_nv()
        print("估值", lof_esti_value.get('gsz'))
        print("折溢价", (float(lof_tick[4]) - float(lof_esti_value.get('gsz')))/(float(lof_tick[4])))
        # 折溢价为百分比值


if __name__ == "__main__":
    diff_lof_price()
