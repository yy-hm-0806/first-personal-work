#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import requests
import json 
url="https://api.yonyoucloud.com/apis/dst/ncov/wholeworld"
header1={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
        ,"authoration":"apicode","apicode":"88ba341661cb4e5da262285c7494899e"}
source=requests.get(url,headers=header1)
result_main=source.text
result = json.loads(source.text)
#print(result_main)
data=result['data']
confirmedCount=data['confirmedCount']
deadCount=data['deadCount']
curedCount=data['curedCount']
updateTime=data['updateTime']
print(confirmedCount,deadCount,curedCount,updateTime)
continent=data['continent']
#Asia=continent['country']
print(continent)


# In[ ]:





# In[5]:


allmess=[]
for item in continent:
    
    #地区=item['continentName']
    ##确诊人数=item['confirmedCount']
    #治愈人数=item['curedCount']
    #死亡人数=item['deadCount']
    国家数=item['country']
    
    for i in range(len(国家数)):
        guojia=[]
        wordmess={}
        wordmess['name']=国家数[i]['provinceName']
        value1['value']=国家数[i]['confirmedCount']
        value2['value']=国家数[i]['curedCount']
        value3['value']=国家数[i]['deadCount']
        guojia.append(国家数[i]['confirmedCount'])
        guojia.append(国家数[i]['curedCount'])
        guojia.append(国家数[i]['deadCount'])
        wordmess['value']=guojia
        allmess.append(wordmess)
print(allmess)


# In[6]:


with open('global_epidemic_statistics3.json', 'w') as f:
    # 先转换成字符串再写入
    #config = json.dumps()
    #f.write(config)
    # 直接写入
    f.write(json.dumps(allmess,ensure_ascii=False))


# In[6]:


with open('global_epidemic_statistics.json', 'r') as f1:
    names = json.load(f1)
print(names)


# In[ ]:




