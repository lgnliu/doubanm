# -*- coding: utf-8 -*-

import random
import base64

from doubanmovie250_tomongodb.settings import PROXIES

# 随机选择代理ip        
class RandomProxy(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)

        # 有用户名密码的代理
        if len(proxy['user_pwd']) != 0:   
            request.meta['proxy'] = 'http://' + proxy['ip_port']
            # 对账户密码进行base64编码
            base64_userpwd = base64.b64encode(proxy['user_pwd'])
            # 对应到代理服务器的信令格式里
            request.headers['Proxy-Authorization'] = 'Basic ' + base64_userpwd
        # 无需用户名密码的代理
        else:
            request.meta['proxy'] = 'http://' + proxy['ip_port']
            print proxy

            
            
    
    
