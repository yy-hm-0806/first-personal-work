#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json


# In[2]:


w=[]
with open("country.txt",'r',encoding="utf-8") as f:
    m=f.readlines()
    for i in m:
        q=[]
        a=i.strip().split(':')
        q.append(a[0])
        q.append(a[1])
        w.append(q)
print(w)


# In[3]:


with open('global_epidemic_statistics3.json','r+') as f1:
    ww=json.load(f1)
    print(ww)


# In[4]:


ww1=[]
with open('global_epidemic_statistics.json','w') as f2:
    for i in range(len(w)):
        for j in range(len(ww)):
            if (w[i][1]==ww[j]['name']):
                ww[j]['name']=w[i][0]
    #with open('global_epidemic_statistics22.json','w') as f3:
        #f.write(json.dumps(ww,ensure_ascii=False,indent=2))
    ww1=ww
print(ww1)


# In[5]:


with open('global_epidemic_statistics44.json','w',encoding='utf-8') as f3
    f3.write(json.dumps(ww1,ensure_ascii=False))


# In[ ]:





# In[ ]:





# In[ ]:




