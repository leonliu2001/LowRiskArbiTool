import pandas as pd
import time
from data.sina_tick import SinaTick
from data.ttjj_data import TtjjData


def diff_lof_nav():
    lof_codes = pd.read_csv('../csv/lof.csv', header=None, index_col=0).squeeze().to_dict()
    # 从csv文件读取lof的代码和名称
    lof_keys = list(lof_codes.keys())  # 取代码为List
    for lof_key in lof_keys:
        lof_no = 'sz' + str(lof_key)    # 增加sz标识
        lof_ticks = SinaTick(lof_no)
        lof_tick = lof_ticks.get_stock()
        lof_esti_values = TtjjData(str(lof_key))
        lof_esti_value = lof_esti_values.get_nv()
        print("基金代码：", str(lof_key), "现价：", lof_tick[4], "估值：", lof_esti_value.get('gsz'))
        print("折溢价为：", (float(lof_tick[4]) - float(lof_esti_value.get('gsz')))/(float(lof_tick[4])))
        print("")

if __name__ == "__main__":
    diff_lof_nav()
