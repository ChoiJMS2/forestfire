# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import geopandas as gpd

import requests
from bs4 import BeautifulSoup
import json
import lxml

from datetime import datetime, timedelta
import time

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import folium
from folium.plugins import MarkerCluster

from google.cloud import bigquery
from utils import credentials
from streamlit_folium import st_folium
import pyproj
import plotly.graph_objs as go

def run_map():
    # 빅쿼리 클라이언트 객체 생성
    client = bigquery.Client(credentials=credentials, project=credentials.project_id)
    # 쿼리 작성
    query = """
     SELECT *
     FROM `forestfire-388501.gangwon.gangwon_code`
     """
    # 쿼리 실행 및 결과를 데이터프레임으로 변환
    gangwon_code = client.query(query).to_dataframe()

    # 쿼리 작성
    query1 = """
     SELECT *
     FROM `forestfire-388501.gangwon.weather_stations`
     """
    # 쿼리 실행 및 결과를 데이터프레임으로 변환
    weather_stations = client.query(query1).to_dataframe()
    weather_stations = weather_stations[
        weather_stations["stnAddress"].str.contains("강원도") & weather_stations["endDate"].isna()]
    weather_stations = weather_stations.reset_index(drop=True)

    map = folium.Map(location=[37.55, 128], zoom_start=8)

    # 기상 관측소 위치 표시
    for index, row in weather_stations.iterrows():
        popup = folium.Popup(row['stnAddress'].split(' ')[-1], max_width=300)
        folium.Marker(
            location=[row['stnLatitude'], row['stnLongitude']],
            popup=popup,
            icon=folium.Icon(icon='info-sign', color='blue')
        ).add_to(map)

    st_folium(map, width=1000)

if __name__ == "__main__":
    run_map()