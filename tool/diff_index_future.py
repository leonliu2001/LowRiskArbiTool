
Created on Tue Apr 26 16:12:55 2022

@author: LeonLiu2001
"""
from datetime import datetime
import pandas as pd
from sina_tick import SinaTick
def diff_index_future():
    future_dict = pd.read_csv('../csv/futures.csv', header=None, index_col=0, squeeze=True).to_dict()
    # 从csv文件读取future的代码和名称
    future_codes = list(future_dict.keys())
    # 取期货代码，类型为List
    today = datetime.now()
    # 取当天日期
    index_code = "sh000905"
    index_tick = SinaTick(index_code)
    index_price = index_tick.get_stock()
    # 取中证500指数实时值
    for future_code in future_codes:
        future_tick = SinaTick(future_code)
        future_price = future_tick.get_cff_future()
        # 取期货实时交易数据
        print("中证500指数现价", index_price[4])
        print(future_code + "期货合约现价", future_price[4])
        settlement_day = datetime.strptime(str(future_dict[future_code]), '%Y%m%d')
        day_count = (settlement_day - today).days + 1
        print("到期天数：", day_count)
        print("贴水率为", (float(index_price[4]) - float(future_price[4]))/(float(index_price[4])))
        print("年化贴水率为", ((float(index_price[4]) - float(future_price[4])) / (float(index_price[4])))*365/day_count)
        print("")
