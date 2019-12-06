#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as ny
import pandas as pd
import matplotlib.pyplot as plt
import requests
import re

def updata(url):
    m=requests.get(url)
    m_txet=m.text
    return m_txet

def bianli(x,y,h):
    url='空'
    for z in y:
        if z[2]==x:
            if h==1:
                url='http://www.tianqihoubao.com/%s' %z[0]
            elif h==2:
                url='http://www.tianqihoubao.com/weather/%s' %z[0]
            z_ming=z[2] 
    if url=='空':
        print("输入有误")
    return url

url='http://www.tianqihoubao.com/'
quanguo=updata(url)
#print(quanguo)
quanguo_1=re.findall(r'cellpadding="1">(.*?)<script async',quanguo,re.S)[0]
# print(quanguo_1)
quanguo_2=re.findall(r'<a href="(.*?)" title="(.*?)">(.*?)</a></td>',quanguo_1,re.S)
# print(quanguo_2)
############################################遍历各个省份#####################################
# for shengfen in quanguo_2:
#     url='http://www.tianqihoubao.com/%s' %shengfen[0]
#     shengfen_ming=shengfen[2]
#     print(url,shengfen_ming)


# In[2]:


print("请输入想要查询的省份：\n")
x1=input()
# x1="广东"
print("请输入查询的县/市：")
# x2='珠海'
x2=input()
##############################################
url=bianli(x1,quanguo_2,1)
# print(url)
shengfen_1=updata(url)
# print(shengfen_1)
shengfen_2=re.findall(r'cellpadding="1">(.*?)<script type=',shengfen_1,re.S)[0]
xian=re.findall(r'<a href="(.*?)" title="(.*?)">(.*?)</a></td>',shengfen_2,re.S)
# print(shengfen_3)


# In[3]:



url=bianli(x2,xian,2)
# print(url)
xian_1=updata(url)
# print(xian_1)
xian_2=re.findall(r'最低温度</b></td>(.*?)<a href="/lishi/',xian_1,re.S)[0]
# print(xian_2)
tianqi=re.findall(r'<tr>(.*?)</tr>',xian_2,re.S)

################################################33
tianqi_ri=re.findall(r'<td ><b><a href=\'(.*?)\'>(.*?)</a> </b></td>\r\n',xian_2,re.S)
# print(tianqi_ri)
########################################################提取天气信息，方法2
# tianqi_1=re.findall(r'<td>(.*?)</td>\r\n',xian_2,re.S)
# print(tianqi_1)
#######################################################提取天气信息，方法一
tianqi_1=re.findall(r'<td >&nbsp;(.*?)</td>\r\n        <td>(.*?)</td>\r\n        <td>(.*?)</td>\r\n        <td>(.*?)</td>\r\n        <td>(.*?)</td>\r\n        <td>&nbsp;(.*?)</td>\r\n',xian_2,re.S)
# print(tianqi_1)
#####################################################显示天气情况
# for x in tianqi_1:
#     print(list(x))
##################################################写入tet文件####################################
z=0
f = open('tianqi.txt','w')
for j in tianqi_ri:
    x=str(j[1])
    f.write(x+str(tianqi_1[z])+'\n')
#     print(j[1],str(tianqi_1[z]))
    z=z+1
    
f.close()
##########################################################

