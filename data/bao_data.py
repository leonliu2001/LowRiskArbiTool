# -*- coding: utf-8 -*-
"""
Created on Thu May  6 08:43:38 2021

@author: Administrator
"""

import baostock as bs
import pandas as pd


class BaostockData:
    #  从baostock获取股票的历史数据
    def __init__(self, code_no: str, start_date: str, end_date: str):
        self.code_no = code_no
        self.start_date = start_date
        self.end_date = end_date

    def get_bao_data(self):
        lg = bs.login()
        # 登陆系统

        print('login respond error_code:'+lg.error_code)
        print('login respond  error_msg:'+lg.error_msg)
        # 显示登陆返回信息
        rs = bs.query_history_k_data_plus(self.code_no,
                                          "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",
                                          start_date=self.start_date, end_date=self.end_date,
                                          frequency="d", adjustflag="3")
        # 获取沪深A股历史K线数据
        # 详细指标参数，参见“历史行情指标参数”章节；“分钟线”参数与“日线”参数不同。“分钟线”不包含指数。
        # 分钟线指标：date,time,code,open,high,low,close,volume,amount,adjustflag
        # 周月线指标：date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg
        # 股票代码格式为 sh.xxxxxx或sz.xxxxxx，日期格式为yyyy-mm-dd
        data_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        result.to_csv('./json/history_A_stock_k_data.csv', index=False)
        # 可以将结果集输出到csv文件，需要先建立一个csv文件
        bs.logout()
        # 登出系统
        return result
