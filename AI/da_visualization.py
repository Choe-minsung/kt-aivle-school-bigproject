#!/usr/bin/env python
# coding: utf-8

# # 데이터 시각화

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False


# In[5]:


df = pd.read_csv('상습예측구간_거리순정렬.csv', encoding = 'utf-8-sig')

df


# In[52]:


df = pd.read_csv('행정안전부_상습 결빙구간_20231222.csv', encoding = 'utf-8-sig')

df


# In[53]:


df['대표지역'].value_counts()


# In[56]:


df = df[['구간 번호', '대표지역']]

df


# In[57]:


df.info()


# In[61]:


cnt = 0

for i in range(len(df)):
    if '원주' in str(df['대표지역'][i]):
        cnt += 1


# In[62]:


cnt


# In[63]:


cnt1 = 0

for i in range(len(df)):
    if '강원' in str(df['대표지역'][i]):
        cnt1 += 1


# In[65]:


cnt1


# In[77]:


g_list = []
cnt2 = 0

for i in range(len(df)):
    if '강원' in str(df['대표지역'][i]):
        g_list.append(df['대표지역'][i].split()[-1])
        cnt2 += 1


# In[87]:


from collections import Counter

g_c = Counter(g_list).most_common()


# In[88]:


g_c


# ### piechart - 전국 / 강원도 / 원주시

# In[145]:


plt.title('전국 / 강원도 / 원주시 결빙구간비율')

ratio = [len(df) - cnt1, cnt1 - cnt, cnt]
labels = ['전국', '강원도', '원주시']
colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}

plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False, colors=colors, wedgeprops=wedgeprops)
plt.show()


# ### piechart2 - 강원도 내 지역

# In[146]:


ratio = []

for i in range(len(g_c) - 4):
    ratio.append(g_c[i][1])
    
ratio.append(51)


# In[147]:


labels = []

for i in range(len(g_c) - 4):
    labels.append(g_c[i][0])
    
labels.append('그 외')


# In[148]:


plt.title('강원도 내 전지역 결빙구간비율')

colors = ['#ffc000', '#ffc000', '#8fd9b6', '#ffc000','#ffc000','#ffc000','#ffc000','#ffc000','#ffc000','#ffc000','#ffc000','#ffc000','#ff9999' ]
wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}

plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False, colors=colors, wedgeprops=wedgeprops)
plt.show()

