import pandas as pd
from sina_tick import SinaTick

csv_file = './json/cbondlist.csv'
csv_data = pd.read_csv(csv_file, low_memory=False, converters={'stcode': str})
csv_df = pd.DataFrame(csv_data)

stock_keys = list(csv_df['cbcode'])
m = len(csv_df.index)
n = 0
while n < m:
    CbondCode = csv_df.loc[n, 'cbcode']
    StockCode = csv_df.loc[n, 'stcode']
    ChangePrice = csv_df.loc[n, 'cprice']

    if str(CbondCode).startswith('11'):  # 挑选上海交易所的股票
        print("转债代码", str(CbondCode))
        CbondCodeSh = 'sh' + str(CbondCode)  # 增加sh标识
        CbondTicksSh = SinaTick(CbondCodeSh)
        CbondTickSh = CbondTicksSh.get_stock()  # 抽取股票当前价格
        print("转债现价", CbondTickSh[4])
        cp = float(CbondTickSh[4])

        if str(StockCode).startswith('60'):
            print("股票代码", str(StockCode))
            StockCodeSh = 'sh' + str(StockCode)  # 增加sh标识
            StockTicksSh = SinaTick(StockCodeSh)
            StockTickSh = StockTicksSh.get_stock()  # 抽取股票当前价格
            print("股票现价", StockTickSh[4])
            sp = float(StockTickSh[4])
            Discount = (cp - ((100 / float(ChangePrice)) * sp)) / (sp * (100 / float(ChangePrice)))
            print("折溢价为：", Discount)

    if str(CbondCode).startswith('12'):  # 挑选深圳交易所的转债
        print("转债代码", str(CbondCode))
        CbondCodeSz = 'sz' + str(CbondCode)  # 增加sz标识
        CbondticksSz = SinaTick(CbondCodeSz)
        CbondTickSz = CbondticksSz.get_stock()
        print("转债现价", CbondTickSz[4])
        cp = float(CbondTickSz[4])

        if str(StockCode).startswith(('00', '30')):  # 挑选深圳交易所的股票
            print("股票代码", str(StockCode))
            StockCodeSz = 'sz' + str(StockCode)  # 增加sz标识
            StockTicksSz = SinaTick(StockCodeSz)
            StockCodeSz = StockTicksSz.get_stock()
            print("股票现价", StockCodeSz[4])
            sp = float(StockCodeSz[4])
            Discount = (cp - ((100 / float(ChangePrice)) * sp)) / (sp * (100 / float(ChangePrice)))
            print("折溢价为：", Discount)

    n = n+1
