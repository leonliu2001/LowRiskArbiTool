import requests


class TencentData:
    """腾讯免费行情获取"""
    def __init__(self, code_no: str):
        self.code_no = code_no

    def get_stock(self):
        # 取股票当前数据
        url = "http://qt.gtimg.cn/q=" + self.code_no
        page = requests.get(url)
        stock_info = page.text
        stock_data = stock_info.split("~")
        stock_dict = {
            "name": stock_data[1],
            "code": stock_data[2],
            "now": float(stock_data[3]),
            "close": float(stock_data[4]),
            "open": float(stock_data[5]),
            "volume": float(stock_data[6]) * 100,
            "bid_volume": int(stock_data[7]) * 100,
            "ask_volume": float(stock_data[8]) * 100,
            "bid1": float(stock_data[9]),
            "bid1_volume": int(stock_data[10]) * 100,
            "bid2": float(stock_data[11]),
            "bid2_volume": int(stock_data[12]) * 100,
            "bid3": float(stock_data[13]),
            "bid3_volume": int(stock_data[14]) * 100,
            "bid4": float(stock_data[15]),
            "bid4_volume": int(stock_data[16]) * 100,
            "bid5": float(stock_data[17]),
            "bid5_volume": int(stock_data[18]) * 100,
            "ask1": float(stock_data[19]),
            "ask1_volume": int(stock_data[20]) * 100,
            "ask2": float(stock_data[21]),
            "ask2_volume": int(stock_data[22]) * 100,
            "ask3": float(stock_data[23]),
            "ask3_volume": int(stock_data[24]) * 100,
            "ask4": float(stock_data[25]),
            "ask4_volume": int(stock_data[26]) * 100,
            "ask5": float(stock_data[27]),
            "ask5_volume": int(stock_data[28]) * 100,
            "最近逐笔成交": stock_data[29],
            "datetime": stock_data[30],
            "涨跌": float(stock_data[31]),
            "涨跌(%)": float(stock_data[32]),
            "high": float(stock_data[33]),
            "low": float(stock_data[34]),
            "价格/成交量(手)/成交额": stock_data[35],
            "成交量(手)": int(stock_data[36]) * 100,
            "成交额(万)": float(stock_data[37]) * 10000,
            "turnover": (stock_data[38]),
            "PE": (stock_data[39]),
            "unknown": stock_data[40],
            "high_2": float(stock_data[41]),  # 意义不明
            "low_2": float(stock_data[42]),  # 意义不明
            "振幅": float(stock_data[43]),
            "流通市值": (stock_data[44]),
            "总市值":(stock_data[45]),
            "PB": float(stock_data[46]),
            "涨停价": float(stock_data[47]),
            "跌停价": float(stock_data[48]),
            "量比": float(stock_data[49]),
            "委差": float(stock_data[50]),
            "均价": float(stock_data[51]),
            "市盈(动)": (stock_data[52]),
            "市盈(静)": stock_data[53]
        }
        return stock_dict
