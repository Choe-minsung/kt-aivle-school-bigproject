
# ==================================== import ====================================
import pandas as pd
import numpy as np
import datetime
import joblib
from keras.models import load_model
from haversine import haversine
from urllib.parse import quote
import streamlit as st
from streamlit_folium import st_folium
import folium
import branca
from geopy.geocoders import Nominatim
import ssl
import plotly.express as px
from urllib.request import urlopen
from geopy.distance import geodesic
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False
from collections import Counter

# ==================================== Layout ====================================
st.set_page_config(layout="wide")

# tabs
t1, t2 = st.tabs(['가격예측', '통계분석'])

# t1
with t1:
    
    st.markdown("# 드론을 활용한 블랙아이스 탐지 솔루션")

    st.image('logo.png')

    now_date = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=9)


    st.markdown("#### 날짜 및 시간 정보")

    col110, col111, col112, col113 = st.columns([0.1, 0.4, 0.1, 0.4])
    with col110:
        st.info("현재 날짜")
    with col111:
        input_date = st.date_input('날짜', label_visibility="collapsed")
    with col112:
        st.info("현재 시간")
    with col113:
        input_time = st.time_input('시간', datetime.time(now_date.hour, now_date.minute), label_visibility="collapsed")

    st.markdown("#### 드론 출발 위치")
    col120, col121 = st.columns([0.1, 0.4])
    with col120:
        st.info("드론 출발 위치")
    with col121:
        location2 = st.selectbox("드론 출발 위치를 선택하세요", 
                                 ("도로교통공단 본부",    # 도로교통공단 본부 - 강원특별자치도 원주시 혁신로 2
                                 "강릉대학교 원주캠퍼스", # 강릉대학교 원주캠퍼스 - 강원특별자치도 원주시 흥업면 남원로 150
                                 "원주 부론산업단지"))    # 부론산업단지 - 강원특별자치도 원주시 부론면 견훤로 640-2



    # 상습결빙구간 탐지 결과
    ice = pd.read_csv("./결빙 지역 감지 결과 1.csv", encoding = "cp949", index_col = 0)

    st.markdown("#### 실시간 결빙 상습/예상 구간")
    st.caption("상위 6개 결빙 지역")
    st.dataframe(ice)


    # ================================================================================  

    # 드론 출동 현황

    Dron = pd.read_csv("./드론 출동 현황.csv", encoding = "cp949", index_col = 0)
    Dron1 = pd.read_csv("./드론 출동 현황1.csv", encoding = "cp949", index_col = 0)
    Dron2 = pd.read_csv("./드론 출동 현황2.csv", encoding = "cp949", index_col = 0)


    st.markdown("#### 실시간 드론 상태 현황")

    st.dataframe(Dron)


    # Folium 맵 1차 객체생성
    # =============================================================================================

    df = pd.read_csv("./1월10일8시_원주시_위도경도_총합.csv", encoding = "utf-8-sig")

    df = {
        'Latitude': df['위도'],
        'Longitude': df['경도'],
    }

    df = pd.DataFrame(df)

    map_center = [37.334794, 127.921739]
    # Create a Folium map object
    my_map = folium.Map(location=map_center, zoom_start=11, width = 1400, height = 1000)
    circle_locations = [
        {'latitude': 37.3244992551977, 'longitude': 127.97535913134},
        {'latitude': 37.3051998482115, 'longitude': 127.922180834517},
        {'latitude': 37.256395635416, 'longitude': 127.780134667723}
    ]

    circle_radius = 7500  # 7.5 km in meters 

    # 반경 원 나타내기 folium.CircleMarker([위도, 경도]).add_to(지도)========================================


    for location in circle_locations:
        folium.Circle(
            location=[location['latitude'], location['longitude']],
            radius=circle_radius,
            color='blue',
            fill=True,
            fill_opacity=0.15
        ).add_to(my_map)

    for index, row in df[:9].iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            icon=folium.Icon(icon = 'flag', color='orange')
        ).add_to(my_map)

    for index, row in df[9:].iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            icon=folium.Icon(icon = 'tower', color='orange')
        ).add_to(my_map)

    st.title('원주시 결빙 상습/예상 구간')
    st.info("2023-01-10 AM 8:00 현황 (flag : 상습결빙구간, tower : 예상결빙구간)")

    st.components.v1.html(my_map._repr_html_(), width=1400, height=1000)


    i = 0

    # 드론 출동 버튼
    if st.button("드론 출동"):


        df = pd.read_csv("./상습예측구간_거리순정렬.csv", encoding = "utf-8-sig")

        df = {
            'Latitude': df['위도'],
            'Longitude': df['경도'],
        }

        df = pd.DataFrame(df)

        map_center = [37.334794, 127.921739]
        # Create a Folium map object
        my_map = folium.Map(location=map_center, zoom_start=11, width = 1400, height = 1000)
        circle_locations = [
            {'latitude': 37.3244992551977, 'longitude': 127.97535913134},
            {'latitude': 37.3051998482115, 'longitude': 127.922180834517},
            {'latitude': 37.256395635416, 'longitude': 127.780134667723}
        ]

        circle_radius = 7500  # 7.5 km in meters 

    # 반경 원 나타내기 folium.CircleMarker([위도, 경도]).add_to(지도) ==============================


        for location in circle_locations:
            folium.Circle(
                location=[location['latitude'], location['longitude']],
                radius=circle_radius,
                color='blue',
                fill=True,
                fill_opacity=0.15
            ).add_to(my_map)

        for index, row in df[0:1].iterrows():
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                icon=folium.Icon(icon = 'tower', color='red')
            ).add_to(my_map)

        for index, row in df[1:2].iterrows():
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                icon=folium.Icon(icon = 'tower', color='gray')
            ).add_to(my_map)

        for index, row in df[2:8].iterrows():
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                icon=folium.Icon(icon = 'tower', color='orange')
            ).add_to(my_map)

        for index, row in df[8:].iterrows():
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                icon=folium.Icon(icon = 'flag', color='orange')
            ).add_to(my_map)


        st.title('원주시 결빙 상습/예상 구간')

        st.warning("드론탐지가 8:46 AM에 완료되었습니다.")

        st.markdown("#### 드론 탐지 결과")

        st.dataframe(Dron1)

        st.info("2023-01-10 AM 8:46 현황 (flag : 상습결빙구간, tower : 예상결빙구간)")

        st.components.v1.html(my_map._repr_html_(), width=1400, height=1000)



        i += 1


    if st.button("드론 출동 "):

        i += 1


        df = pd.read_csv("./상습예측구간_거리순정렬.csv", encoding = "utf-8-sig")

        df = {
            'Latitude': df['위도'],
            'Longitude': df['경도'],
        }

        df = pd.DataFrame(df)

        map_center = [37.334794, 127.921739]

        my_map = folium.Map(location=map_center, zoom_start=11, width = 1400, height = 1000)
        circle_locations = [
            {'latitude': 37.3244992551977, 'longitude': 127.97535913134},
            {'latitude': 37.3051998482115, 'longitude': 127.922180834517},
            {'latitude': 37.256395635416, 'longitude': 127.780134667723}
        ]

        circle_radius = 7500  # 7.5 km in meters 

    # 반경 원 나타내기 folium.CircleMarker([위도, 경도]).add_to(지도) ==============================


        for location in circle_locations:
            folium.Circle(
                location=[location['latitude'], location['longitude']],
                radius=circle_radius,
                color='blue',
                fill=True,
                fill_opacity=0.15
            ).add_to(my_map)

        for index, row in df[0:1].iterrows():

            html = """<!DOCTYPE html>
                        <html>
                            <table style="height: 126px; width: 330px;"> <tbody> <tr>
                                <td style="background-color: #2A799C;">
                                <div style="color: #ffffff;text-align:center;">위도</div></td>
                                <td style="width: 230px;background-color: #C5DCE7;">{}</td>""".format(ice['위도'][0])+"""</tr>
                                <tr><td style="background-color: #2A799C;">
                                <div style="color: #ffffff;text-align:center;">경도</div></td>
                                <td style="width: 230px;background-color: #C5DCE7;">{}</td>""".format(ice['경도'][0])+"""</tr>
                                <tr><td style="background-color: #2A799C;">
                                <div style="color: #ffffff;text-align:center;">거리(km)</div></td>
                                <td style="width: 230px;background-color: #C5DCE7;">{}</td>""".format(ice['거리(km)'][0])+""" </tr>
                            </tbody> </table> </html> """

            iframe = branca.element.IFrame(html=html, width=350, height=150)
            popup_text = folium.Popup(iframe,parse_html=True)

            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                popup=popup_text, tooltip=ice['주소(지역)'][0],
                icon=folium.Icon(icon = 'tower', color='red')
            ).add_to(my_map)

        for index, row in df[1:2].iterrows():
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                icon=folium.Icon(icon = 'tower', color='gray')
            ).add_to(my_map)

        for index, row in df[2:3].iterrows():
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                icon=folium.Icon(icon = 'tower', color='red')
            ).add_to(my_map)

        for index, row in df[3:8].iterrows():
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                icon=folium.Icon(icon = 'tower', color='orange')
            ).add_to(my_map)

        for index, row in df[8:9].iterrows():
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                icon=folium.Icon(icon = 'flag', color='red')
            ).add_to(my_map)

        for index, row in df[9:].iterrows():
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                icon=folium.Icon(icon = 'flag', color='orange')
            ).add_to(my_map)

        st.title('원주시 결빙 상습/예상 구간')

        st.warning("드론탐지가 9:32 AM에 완료되었습니다.")

        st.markdown("#### 드론 탐지 결과")

        st.dataframe(Dron2)

        st.info("2023-01-10 AM 9:32 현황 (flag : 상습결빙구간, tower : 예상결빙구간)")

        st.components.v1.html(my_map._repr_html_(), width=1400, height=1000)



    elif i == 2:
        st.dataframe(Dron2)

with t2:
    st.markdown("# 원주시 결빙구간 분석")
    
    st.image('logo.png')
    
    st.error("통계 분석")
    
    df_a = pd.read_csv('행정안전부_상습 결빙구간_20231222.csv', encoding = 'utf-8-sig')
    
    df_a = df_a[['구간 번호', '대표지역']]

    cnt = 0
    cnt1 = 0
    cnt2 = 0
    g_list = []

    for i in range(len(df_a)):
        if '원주' in str(df_a['대표지역'][i]):
            cnt += 1

    for i in range(len(df_a)):
        if '강원' in str(df_a['대표지역'][i]):
            cnt1 += 1

    for i in range(len(df_a)):
        if '강원' in str(df_a['대표지역'][i]):
            g_list.append(df_a['대표지역'][i].split()[-1])
            cnt2 += 1

    g_c = Counter(g_list).most_common()

    ratio = []

    for i in range(len(g_c) - 4):
        ratio.append(g_c[i][1])

    ratio.append(51)

    labels = []

    for i in range(len(g_c) - 4):
        labels.append(g_c[i][0])

    labels.append('그 외')

    df_1 = pd.DataFrame({"지역": labels, "도수" : ratio})

    ratio_1 = [len(df_a) - cnt1, cnt1 - cnt, cnt]
    labels_1 = ['전국', '강원도', '원주시']

    df_2 = pd.DataFrame({"지역": labels_1, "도수" : ratio_1})
    
    c1, c2 = st.columns([0.45, 0.45])
    
    with c1:
        fig = px.pie(df_2, names='지역', values='도수', title = '전국 / 강원도 / 원주시 결빙구간비율' , hole = 0.3)
        fig.update_traces(textposition = 'inside', textinfo = 'percent + label')
        fig.update_layout(font=dict(size=18))
        st.plotly_chart(fig)

    with c2:
        fig = px.pie(df_1, names='지역', values='도수', title = '강원도 내 전지역 결빙구간비율' , hole = 0.3)
        fig.update_traces(textposition = 'inside', textinfo = 'percent + label')
        fig.update_layout(font=dict(size=18))
        st.plotly_chart(fig)
