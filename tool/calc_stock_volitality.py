import numpy as np
import math
from bao_data import BaostockData

# 以601166为例，计算波动率，时间选择一整年

n = 242
# 计算n天波动率，需要n+1天数据，按一年243个交易日（因为农历假期的原因，365天内交易日可能不相同），日期设置可间隔1整年
bt = BaostockData("sh.600519", "2021-06-06", "2022-06-06")
# 实例化BaostockDate类，证券代码格式为sh.xxxxxx或sz.xxxxxx
history_data = bt.get_bao_data()
diff_ln_total = []
try:
    for i in range(n):

        yestoday_close = history_data.iloc[i - n - 1].close
        print(yestoday_close)

        today_close = history_data.iloc[i - n].close
        print(today_close)
        # 计算对数
        ln_yestoday_close = math.log(float(yestoday_close), math.e)
        ln_today_close = math.log(float(today_close), math.e)
        # 计算对数差并传入数组
        diff_ln = ln_yestoday_close - ln_today_close
        diff_ln_total.append(diff_ln)
    std_dev = np.std(diff_ln_total, ddof=1)  # 使用样本计算标准差
    print("标准差为 %f" %std_dev)
    volitality = std_dev * math.sqrt(243)
    # 计算volitality,年交易日按243个交易日
    print("年化波动率为 %f" %volitality)
except:
    print("未取到数据，请调整起始和终止日期值")
