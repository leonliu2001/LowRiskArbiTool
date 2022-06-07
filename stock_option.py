# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 14:12:11 2022

@author: Administrator
"""

import numpy as np
from scipy.stats import norm
from math import *
from numpy.random import standard_normal
from math import exp, sqrt


class StockOption:
    def __init__(self, S: float, K: float, r: float, sigma: float, t: float, n: int):
        #  S为现价，X为目标价格， r为利率， sigma为波动率，t为时间， n为模拟次数
        self.S = S
        self.K = K
        self.r = r
        self.sigma = sigma
        self.t = t
        self.n = n

    def call_montecarlo(self):

        """欧式期权的蒙特卡洛定价公式"""
        z = standard_normal(self.n)
        St = self.S*np.exp((self.r-0.5*self.sigma**2)*self.t+self.sigma*z*np.sqrt(self.t))
        return sum(np.maximum(0, St-self.K))*(np.exp(-self.r*self.t))/self.n

    def put_montecarlo(self):
        z = standard_normal(self.n)
        St = self.S*np.exp((self.r-0.5*self.sigma**2)*self.t+self.sigma*z*np.sqrt(self.t))
        return sum(np.maximum(0, self.K-St))*(np.exp(-self.r*self.t))/self.n

    def call_bsm(self):
        """欧式期权的bs定价公式"""
        d1 = (log(self.S/self.K)+(self.r+self.sigma**2/2)*self.t)/(self.sigma*sqrt(self.t))
        d2 = d1-self.sigma*sqrt(self.t)
        c = self.S*norm.cdf(d1)-self.K*exp(-self.r*self.t)*norm.cdf(d2)
        return c

    def put_bsm(self):
        d1 = (log(self.S/self.K)+(self.r+self.sigma**2/2)*self.t)/(self.sigma*sqrt(self.t))
        d2 = d1-self.sigma*sqrt(self.t)
        p = self.K*exp(-self.r*self.t)*norm.cdf(-d2)-self.S*norm.cdf(-d1)
        return p


if __name__ == "__main__":
    s = StockOption(100, 110, 0.025, 0.22, 1, 10000)
    c1 = s.call_bsm()
    c2 = s.call_montecarlo()
    c4 = s.put_bsm()
    c5 = s.put_montecarlo()
    print(c1)
    print(c2)
    print(c4)
    print(c5)
