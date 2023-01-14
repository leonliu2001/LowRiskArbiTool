#!/usr/bin/env python                                                                                   
#  -*- coding: utf-8 -*-                                                                                
from tqsdk import TqApi, TqAuth                                                                         
                                                                                                        
#从天勤获取期货实时数据，需要安装tqsdk                                                                                                    
class TqTick:                                                                                           
    def __init__(self, code_no: str):                                                                   
        self.code_no = code_no                                                                          
                                                                                                        
    def get_CFFEX_tick(self):                                                                           
        # 创建API实例,传入自己的信易账户                                                                             
        api = TqApi(auth=TqAuth("user", "passwrod"))                                           
        # 获得中金所 IF主力 的行情引用，当行情有变化时 quote 中的字段会对应更新                                                      
        quota = api.get_quote("CFFEX."+self.code_no)                                                    
        # 关闭api,释放资源                                                                                    
        api.close()                                                                                     
        # 返回该品种的最新价                                                                                     
        return quota.last_price                                                                         
                                                                                                                                                                                                                
