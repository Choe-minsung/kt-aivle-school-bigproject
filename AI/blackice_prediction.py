#!/usr/bin/env python
# coding: utf-8

# # blackice_prediction

# ### References
# 
# 1. 기상청 API : 원주시 기온, 습도 data
# - 조사기간 : 2023-01-01 ~ 2023-01-31  
# https://data.kma.go.kr/data/rmt/rmtList.do?code=410&pgmNo=571
# https://data.kma.go.kr/data/grnd/selectAsosRltmList.do?pgmNo=36
# 
# 2. 도로 결빙 예측 Paper
# - 결빙생성 조건  
# https://scienceon.kisti.re.kr/commons/util/originalView.do?cn=JAKO202102763716550&oCn=JAKO202102763716550&dbt=JAKO&journal=NJOU00580137&keyword=%EB%8F%84%EB%A1%9C%20%EA%B2%B0%EB%B9%99

# ### data info

# - df_T_1 ~ df_T_12 : 명륜2동 ~ 행구동의 기온(대기온도) df
# - df_H_1 ~ df_H_12 : 명륜2동 ~ 행구동의 습도 df
# - df : 지면온도 df

# In[1]:


import pandas as pd
import datetime


# # 1. df 생성

# In[2]:


df = pd.read_csv(r"C:\Users\user\Downloads\원주_2023_기상자료.csv", encoding = 'cp949')

df = df[['일시', '지면온도(°C)', '이슬점온도(°C)']]

df = df[9:743]

df


# In[3]:


df.info()


# In[4]:


df['일시'] = pd.to_datetime(df['일시'])


# In[5]:


dong = ['개운동', '귀래면', '단계동', '단구동', '명륜1동',
    '명륜2동',  '무실동', '문막읍', '반곡관설동', '봉산동',
        '부론면', '소초면', '신림면', '우산동', '원인동',
        '일산동', '중앙동', '지정면', '태장1동', '태장2동',
        '판부면', '학성동', '행구동', '호저면', '흥업면']

path = "C:\\Users\\user\\Desktop\\데이터\\"

df_T_1 = pd.read_csv(path + dong[0] + '_기온_20230101_20230131.csv')
df_T_2 = pd.read_csv(path +  dong[1] + '_기온_20230101_20230131.csv')
df_T_3 = pd.read_csv(path + dong[2] + '_기온_20230101_20230131.csv')
df_T_4 = pd.read_csv(path + dong[3] + '_기온_20230101_20230131.csv')
df_T_5 = pd.read_csv(path + dong[4] + '_기온_20230101_20230131.csv')
df_T_6 = pd.read_csv(path + dong[5] + '_기온_20230101_20230131.csv')
df_T_7 = pd.read_csv(path + dong[6] + '_기온_20230101_20230131.csv')
df_T_8 = pd.read_csv(path + dong[7] + '_기온_20230101_20230131.csv')
df_T_9 = pd.read_csv(path + dong[8] + '_기온_20230101_20230131.csv')
df_T_10 = pd.read_csv(path + dong[9] + '_기온_20230101_20230131.csv')
df_T_11 = pd.read_csv(path + dong[10] + '_기온_20230101_20230131.csv')
df_T_12 = pd.read_csv(path + dong[11] + '_기온_20230101_20230131.csv')
df_T_13 = pd.read_csv(path + dong[12] + '_기온_20230101_20230131.csv', encoding = 'utf-8-sig')
df_T_14 = pd.read_csv(path + dong[13] + '_기온_20230101_20230131.csv', encoding = 'utf-8-sig')
df_T_15 = pd.read_csv(path + dong[14] + '_기온_20230101_20230131.csv', encoding = 'utf-8-sig')
df_T_16 = pd.read_csv(path + dong[15] + '_기온_20230101_20230131.csv', encoding = 'utf-8-sig')
df_T_17 = pd.read_csv(path + dong[16] + '_기온_20230101_20230131.csv', encoding = 'utf-8-sig')
df_T_18 = pd.read_csv(path + dong[17] + '_기온_20230101_20230131.csv', encoding = 'utf-8-sig')
df_T_19 = pd.read_csv(path + dong[18] + '_기온_20230101_20230131.csv', encoding = 'utf-8-sig')
df_T_20 = pd.read_csv(path + dong[19] + '_기온_20230101_20230131.csv', encoding = 'utf-8-sig')
df_T_21 = pd.read_csv(path + dong[20] + '_기온_20230101_20230131.csv', encoding = 'utf-8-sig')
df_T_22 = pd.read_csv(path + dong[21] + '_기온_20230101_20230131.csv', encoding = 'utf-8-sig')
df_T_23 = pd.read_csv(path + dong[22] + '_기온_20230101_20230131.csv', encoding = 'utf-8-sig')
df_T_24 = pd.read_csv(path + dong[23] + '_기온_20230101_20230131.csv', encoding = 'utf-8-sig')
df_T_25 = pd.read_csv(path + dong[24] + '_기온_20230101_20230131.csv', encoding = 'utf-8-sig')


# In[6]:


dong = ['개운동', '귀래면', '단계동', '단구동', '명륜1동',
    '명륜2동',  '무실동', '문막읍', '반곡관설동', '봉산동',
        '부론면', '소초면', '신림면', '우산동', '원인동',
        '일산동', '중앙동', '지정면', '태장1동', '태장2동',
        '판부면', '학성동', '행구동', '호저면', '흥업면']

path = "C:\\Users\\user\\Desktop\\데이터\\"

df_H_1 = pd.read_csv(path + dong[0] + '_습도_20230101_20230131.csv')
df_H_2 = pd.read_csv(path +  dong[1] + '_습도_20230101_20230131.csv')
df_H_3 = pd.read_csv(path + dong[2] + '_습도_20230101_20230131.csv')
df_H_4 = pd.read_csv(path + dong[3] + '_습도_20230101_20230131.csv')
df_H_5 = pd.read_csv(path + dong[4] + '_습도_20230101_20230131.csv')
df_H_6 = pd.read_csv(path + dong[5] + '_습도_20230101_20230131.csv')
df_H_7 = pd.read_csv(path + dong[6] + '_습도_20230101_20230131.csv')
df_H_8 = pd.read_csv(path + dong[7] + '_습도_20230101_20230131.csv')
df_H_9 = pd.read_csv(path + dong[8] + '_습도_20230101_20230131.csv')
df_H_10 = pd.read_csv(path + dong[9] + '_습도_20230101_20230131.csv')
df_H_11 = pd.read_csv(path + dong[10] + '_습도_20230101_20230131.csv')
df_H_12 = pd.read_csv(path + dong[11] + '_습도_20230101_20230131.csv')
df_H_13 = pd.read_csv(path + dong[12] + '_습도_20230101_20230131.csv', encoding = 'utf-8-sig')
df_H_14 = pd.read_csv(path + dong[13] + '_습도_20230101_20230131.csv', encoding = 'utf-8-sig')
df_H_15 = pd.read_csv(path + dong[14] + '_습도_20230101_20230131.csv', encoding = 'utf-8-sig')
df_H_16 = pd.read_csv(path + dong[15] + '_습도_20230101_20230131.csv', encoding = 'utf-8-sig')
df_H_17 = pd.read_csv(path + dong[16] + '_습도_20230101_20230131.csv', encoding = 'utf-8-sig')
df_H_18 = pd.read_csv(path + dong[17] + '_습도_20230101_20230131.csv', encoding = 'utf-8-sig')
df_H_19 = pd.read_csv(path + dong[18] + '_습도_20230101_20230131.csv', encoding = 'utf-8-sig')
df_H_20 = pd.read_csv(path + dong[19] + '_습도_20230101_20230131.csv', encoding = 'utf-8-sig')
df_H_21 = pd.read_csv(path + dong[20] + '_습도_20230101_20230131.csv', encoding = 'utf-8-sig')
df_H_22 = pd.read_csv(path + dong[21] + '_습도_20230101_20230131.csv', encoding = 'utf-8-sig')
df_H_23 = pd.read_csv(path + dong[22] + '_습도_20230101_20230131.csv', encoding = 'utf-8-sig')
df_H_24 = pd.read_csv(path + dong[23] + '_습도_20230101_20230131.csv', encoding = 'utf-8-sig')
df_H_25 = pd.read_csv(path + dong[24] + '_습도_20230101_20230131.csv', encoding = 'utf-8-sig')


# In[7]:


for i in range(1,26):
    eval(f'df_T_{i}').columns = ['측정일', '측정시간', 'forecast', '기온']
    display(eval(f'df_T_{i}'))


# In[8]:


for i in range(1,26):
    eval(f'df_H_{i}').columns = ['측정일', '측정시간', 'forecast', '습도']
    display(eval(f'df_H_{i}'))


# In[9]:


# list 형태로 온,습도 df 저장

T = [eval(f'df_T_{i}') for i in range(1,26)]
H = [eval(f'df_H_{i}') for i in range(1,26)]


# # 2. df 전처리
# 
# 1. forecast(세부지역) 평균으로 온,습도 df concat
# 2. IQR방식 이상치 처리
# 3. 협정세계시와 한국표준시 통일(9시간 30분), 지면온도 df와 mapping
# 4. 측정일기준 1/1 10:00부터 사용

# 1. forecast(세부지역) 평균으로 온도df, 습도df concat

# In[10]:


# df_W_{i} : 온,습도 df

df_W_1 = pd.concat([T[0], H[0]], axis=1).iloc[:,[0,1,2,3,7]].groupby(['측정일', '측정시간'])['기온', '습도'].mean().reset_index(drop = False)
df_W_2 = pd.concat([T[1], H[1]], axis=1).iloc[:,[0,1,2,3,7]].groupby(['측정일', '측정시간'])['기온', '습도'].mean().reset_index(drop = False)
df_W_3 = pd.concat([T[2], H[2]], axis=1).iloc[:,[0,1,2,3,7]].groupby(['측정일', '측정시간'])['기온', '습도'].mean().reset_index(drop = False)
df_W_4 = pd.concat([T[3], H[3]], axis=1).iloc[:,[0,1,2,3,7]].groupby(['측정일', '측정시간'])['기온', '습도'].mean().reset_index(drop = False)
df_W_5 = pd.concat([T[4], H[4]], axis=1).iloc[:,[0,1,2,3,7]].groupby(['측정일', '측정시간'])['기온', '습도'].mean().reset_index(drop = False)
df_W_6 = pd.concat([T[5], H[5]], axis=1).iloc[:,[0,1,2,3,7]].groupby(['측정일', '측정시간'])['기온', '습도'].mean().reset_index(drop = False)
df_W_7 = pd.concat([T[6], H[6]], axis=1).iloc[:,[0,1,2,3,7]].groupby(['측정일', '측정시간'])['기온', '습도'].mean().reset_index(drop = False)
df_W_8 = pd.concat([T[7], H[7]], axis=1).iloc[:,[0,1,2,3,7]].groupby(['측정일', '측정시간'])['기온', '습도'].mean().reset_index(drop = False)
df_W_9 = pd.concat([T[8], H[8]], axis=1).iloc[:,[0,1,2,3,7]].groupby(['측정일', '측정시간'])['기온', '습도'].mean().reset_index(drop = False)
df_W_10 = pd.concat([T[9], H[9]], axis=1).iloc[:,[0,1,2,3,7]].groupby(['측정일', '측정시간'])['기온', '습도'].mean().reset_index(drop = False)
df_W_11 = pd.concat([T[10], H[10]], axis=1).iloc[:,[0,1,2,3,7]].groupby(['측정일', '측정시간'])['기온', '습도'].mean().reset_index(drop = False)
df_W_12 = pd.concat([T[11], H[11]], axis=1).iloc[:,[0,1,2,3,7]].groupby(['측정일', '측정시간'])['기온', '습도'].mean().reset_index(drop = False)
df_W_13 = pd.concat([T[12], H[12]], axis=1).iloc[:,[0,1,2,3,7]].groupby(['측정일', '측정시간'])['기온', '습도'].mean().reset_index(drop = False)
df_W_14 = pd.concat([T[13], H[13]], axis=1).iloc[:,[0,1,2,3,7]].groupby(['측정일', '측정시간'])['기온', '습도'].mean().reset_index(drop = False)
df_W_15 = pd.concat([T[14], H[14]], axis=1).iloc[:,[0,1,2,3,7]].groupby(['측정일', '측정시간'])['기온', '습도'].mean().reset_index(drop = False)
df_W_16 = pd.concat([T[15], H[15]], axis=1).iloc[:,[0,1,2,3,7]].groupby(['측정일', '측정시간'])['기온', '습도'].mean().reset_index(drop = False)
df_W_17 = pd.concat([T[16], H[16]], axis=1).iloc[:,[0,1,2,3,7]].groupby(['측정일', '측정시간'])['기온', '습도'].mean().reset_index(drop = False)
df_W_18 = pd.concat([T[17], H[17]], axis=1).iloc[:,[0,1,2,3,7]].groupby(['측정일', '측정시간'])['기온', '습도'].mean().reset_index(drop = False)
df_W_19 = pd.concat([T[18], H[18]], axis=1).iloc[:,[0,1,2,3,7]].groupby(['측정일', '측정시간'])['기온', '습도'].mean().reset_index(drop = False)
df_W_20 = pd.concat([T[19], H[19]], axis=1).iloc[:,[0,1,2,3,7]].groupby(['측정일', '측정시간'])['기온', '습도'].mean().reset_index(drop = False)
df_W_21 = pd.concat([T[20], H[20]], axis=1).iloc[:,[0,1,2,3,7]].groupby(['측정일', '측정시간'])['기온', '습도'].mean().reset_index(drop = False)
df_W_22 = pd.concat([T[21], H[21]], axis=1).iloc[:,[0,1,2,3,7]].groupby(['측정일', '측정시간'])['기온', '습도'].mean().reset_index(drop = False)
df_W_23 = pd.concat([T[22], H[22]], axis=1).iloc[:,[0,1,2,3,7]].groupby(['측정일', '측정시간'])['기온', '습도'].mean().reset_index(drop = False)
df_W_24 = pd.concat([T[23], H[23]], axis=1).iloc[:,[0,1,2,3,7]].groupby(['측정일', '측정시간'])['기온', '습도'].mean().reset_index(drop = False)
df_W_25 = pd.concat([T[24], H[24]], axis=1).iloc[:,[0,1,2,3,7]].groupby(['측정일', '측정시간'])['기온', '습도'].mean().reset_index(drop = False)


# 2. IQR방식 이상치처리

# In[11]:


# IQR 계산

quartile_1 = eval(f'df_W_{i}')['기온'].quantile(0.25)
quartile_3 = eval(f'df_W_{i}')['기온'].quantile(0.75)

IQR = quartile_3 - quartile_1


# In[12]:


# 이상치 제거

for i in range(1, 26):
    eval(f'df_W_{i}').drop(eval(f'df_W_{i}')[(eval(f'df_W_{i}')['기온'] < (quartile_1 - 1.5 * IQR)) | (eval(f'df_W_{i}')['기온'] > (quartile_3 + 1.5 * IQR))].index, axis = 0, inplace = True)
    eval(f'df_W_{i}').reset_index(drop = True, inplace = True)
    display(eval(f'df_W_{i}'))


# 3. 협정세계시와 한국표준시 통일(9시간 30분), 지면온도df mapping

# In[13]:


for i in range(1, 26):
    eval(f'df_W_{i}')['측정일'] = eval(f'df_W_{i}')['측정일'].astype(int)


# In[14]:


for i in range(1, 26):
    eval(f'df_W_{i}').sort_values(['측정일', '측정시간'], inplace=True)
    eval(f'df_W_{i}').reset_index(drop=True, inplace=True)


# In[15]:


for i in range(1, 26):
    eval(f'df_W_{i}')['측정시간'] += 970
    eval(f'df_W_{i}').loc[eval(f'df_W_{i}')['측정시간']>=2400, '측정시간'] = eval(f'df_W_{i}')['측정시간']-2400
    eval(f'df_W_{i}').loc[eval(f'df_W_{i}')['측정시간']<=900, '측정일'] = eval(f'df_W_{i}')['측정일']+1


# In[16]:


for i in range(1, 26):
    eval(f'df_W_{i}')['측정시간'] = eval(f'df_W_{i}')['측정시간'].astype('str')
    eval(f'df_W_{i}')['측정시간'] = eval(f'df_W_{i}')['측정시간'].str[:-2]


# In[17]:


for i in range(1, 26):
    eval(f'df_W_{i}')['측정시간'] = eval(f'df_W_{i}')['측정시간'].str[:-2]


# In[18]:


for i in range(1, 26):
    _index = eval(f'df_W_{i}').loc[eval(f'df_W_{i}')['측정일']>31].index
    eval(f'df_W_{i}').drop(_index, inplace=True)
    display(eval(f'df_W_{i}'))


# In[19]:


for i in range(1, 26):
    eval(f'df_W_{i}')['측정시간'] = eval(f'df_W_{i}')['측정시간'].apply(lambda x : str(x).zfill(2))


# # 3. 데이터 병합
# 
# - df와 df_W_n 병합

# In[20]:


for i in range(1, 26):
    eval(f'df_W_{i}')['측정일'] = eval(f'df_W_{i}')['측정일'].astype('str').apply(lambda x : str(x).zfill(2))


# In[21]:


df_W_1


# In[22]:


for i in range(1, 26):
    eval(f'df_W_{i}')['일시'] = eval(f'df_W_{i}')['측정일'] + eval(f'df_W_{i}')['측정시간']


# In[23]:


for i in range(1, 26):
    eval(f'df_W_{i}')['일시'] = '202301' + eval(f'df_W_{i}')['일시'] + '00'


# In[24]:


for i in range(1, 26):
    eval(f'df_W_{i}')['일시'] = pd.to_datetime(eval(f'df_W_{i}')['일시'], format='%Y%m%d%H%M')


# In[25]:


for i in range(1, 26):
    eval(f'df_W_{i}').drop(['측정일', '측정시간'], axis=1, inplace=True)


# In[26]:


mg_data = [pd.merge(df, eval(f'df_W_{i}'), on = '일시', how = 'outer') for i in range(1, 26)]


# In[27]:


for i in range(25):
    display(mg_data[i])


# # 4. 결빙구간 조건 필터링
# 
# - 대기온도 <= 5도
# - 노면온도 <= 0도
# - (기온 – 노면온도) >= 5도
# - 습도 >= 65%

# In[28]:


for i in range(25):
    mg_data[i]['온도차'] = mg_data[i]['지면온도(°C)'] - mg_data[i]['이슬점온도(°C)']
    display(mg_data[i])


# In[37]:


weather = [mg_data[i][(mg_data[i]['기온']<=5) & (mg_data[i]['습도']>=65) & (mg_data[i]['지면온도(°C)']<=0) & (mg_data[i]['온도차']<=5)].reset_index(drop=True) for i in range(25)]


# In[41]:


weather[24]


# In[40]:


for i in range(25):
    weather[i]['shift_4'] = pd.to_datetime(weather[i]['일시'].shift(periods=4), errors='coerce')


# In[42]:


for i in range(25):
    weather[i]['4시간차'] = weather[i]['일시']+datetime.timedelta(hours=-4)


# In[49]:


pred = [weather[i][weather[i]['4시간차']==weather[i]['shift_4']] for i in range(25)]


# In[50]:


pred[24]


# In[52]:


for i in range(25):
    pred[i].to_csv(dong[i] +".csv", index = False, encoding = 'cp949')

