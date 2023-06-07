# -*- coding:utf-8 -*-
import pandas as pd
import calendar

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import streamlit as st
from pathlib import Path

import seaborn as sns
import matplotlib.pyplot as plt
from data import load_data
from google.cloud import bigquery
from utils import credentials
from map import run_map

import folium
from streamlit_folium import st_folium

@st.cache_data(ttl=600)
def run_heatmap():
    # 빅쿼리 클라이언트 객체 생성
    client = bigquery.Client(credentials=credentials, project=credentials.project_id)
    # 쿼리 작성
    project_id = 'forestfire-389107'
    dataset_id = 'PreProcessing_Data'
    table_id = 'weather_stations'
    query = f"""
    SELECT *
    FROM `{project_id}.{dataset_id}.{table_id}`
    """
    # 쿼리 실행 및 결과를 데이터프레임으로 변환
    combined_df = client.query(query).to_dataframe()
    # 상관계수 행렬 계산
    correlation_matrix = combined_df.corr(method='pearson')
    # 히트맵 그리기
    plt.figure(figsize=(14, 12))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 8})
    plt.title('Correlation Heatmap')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
def run_chart2():
    run_map()
def run_chart3():
    # center on Liberty Bell, add marker
    m = folium.Map(location=[37.5666805, 126.9784147], zoom_start=13)
    folium.Marker(
        [37.5666805, 126.9784147], popup="Liberty Bell", tooltip="Liberty Bell"
    ).add_to(m)

    # call to render Folium map in Streamlit
    st_folium(m, width=725)
def run_chart4():
    pass

def run_eda():
    st.sidebar.markdown("## Exploration for Data")
    eda = st.sidebar.radio('submenu',['Chart1', 'Chart2', 'Chart3', 'Chart4'], label_visibility='collapsed')
    if eda == 'Chart1':
        st.markdown("## Chart1")
        run_heatmap()
    elif eda == 'Chart2':
        st.markdown("## Chart2")
        st.warning("please EDA")
        run_chart2()
    elif eda == 'Chart3':
        st.markdown("## Chart3")
        st.warning("please EDA")
        run_chart3()
    elif eda == 'Chart4':
        st.markdown("## Chart4")
        st.warning("please EDA")
        run_chart4()