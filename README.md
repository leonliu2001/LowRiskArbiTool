# LowRiskArbiTool
一个将低风险投资品种的数据进行收集，整理，分析，并将部分品种间存在的套利计算做成工具。
数据获取来源有新浪财经、天天基金网等，实时数据从新浪获取，基金估值从天天基金获取。
编程语言选用python3.7.0，数据库选用了mysql5.7.32，图形界面采用tkinter，ORM采用peewee
sina_tick完成了从新浪财经接口提取股票、期货期权、etf期权的实时成交数据。
