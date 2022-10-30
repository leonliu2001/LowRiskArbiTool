from datetime import datetime
import pandas as pd
from data.sina_tick import SinaTick


def diff_index_option_io():
    option_df = pd.read_csv('../csv/option_io.csv', low_memory=False)
    # 从csv文件读取option的代码和名称
    today = datetime.now()
    # 取当天日期
    i = 0
    while i < 5:
        sp = SinaTick(option_df.values[i, 0])
        print("沽权", option_df.values[i, 0], sp.get_opti()[3])
        sc = SinaTick(option_df.values[i, 1])
        print("购权", option_df.values[i, 1], sc.get_opti()[3])
        strike_price = option_df.values[i, 0][12:16]
        # 取期权标定值
        complex_call = float((sc.get_opti()[3])) - float(sp.get_opti()[3]) + float(strike_price)
        print("期权合成折算指数", complex_call)
        index_code = "sh000300"
        index_tick = SinaTick(index_code)
        index_price = index_tick.get_stock()
        settlement_day = datetime.strptime(str(option_df.values[i, 2]), '%Y%m%d')
        day_count = (settlement_day - today).days + 1
        print("沪深300指数现价：", index_price[4], "到期天数：", day_count)
        print("贴水为：", (float(index_price[4]) - complex_call), "年化贴水率为：", ((float(index_price[4]) -
                                                                         complex_call)/ (float(index_price[4]))*365/day_count))
        print("")
        i = i+1


if __name__ == "__main__":
    diff_index_option_io()
