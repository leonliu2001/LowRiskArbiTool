# LowRiskArbiTool
一个将低风险投资品种的数据进行收集，整理，分析，并将部分品种间存在的套利计算做成工具。<br>
数据获取来源有新浪财经、天天基金网、baostock等，实时数据从新浪获取，基金估值从天天基金获取，历史数据从baostock获取。<br>
编程语言选用python3.7.0，图形界面采用tkinter，数据库选用了mysql5.7.32（暂不涉及），ORM采用peewee（暂不涉及）。<br>
main/menu_window为tkinter图形界面，将相关工具图形化，截至8月2日，仍有部分功能待开发。<br>
data/sina_tick类实现了从新浪财经接口提取股票、期货期权、商品期货、etf期权的实时成交数据，以及提取基金的每日净值数据。<br>
data/ttjj_data类实现了从天天基金网接口提取lof基金的实时估算值。<br>
data/bao_data类实现了从baostock提取股票的历史数据。<br>
data/tencent_data类实现了从腾讯接口提取股票的实时数据。<br>
tool/stock_option类实现用蒙特卡洛、bsm方式对股票的期权定价进行计算。<br>
tool/send_wechat使用163邮箱（开启smtp功能）向qq邮箱发送邮件，在微信端开启qq邮箱提醒功能，实现重要消息提醒（实测延时约10秒)。<br>
tool/diff_lof_price实现比较lof现价和估算值之间的折溢价。<br>
tool/calc_stock_volitality实现了对股票年化波动率的计算，历史数据取自baostock。<br>
tool/diff_index_future实现了比较中证500指数和IC期货，计算IC期货的贴水率。<br>
tool/calc_change_ratio实现了计算可转债转股后价格和正股价格的折溢价率。<br>
