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
from data.map_data import map_loadData
@st.cache_data(ttl=600)
def run_map():
    forestfire_occurs, weather_stations, gangwon_code, gangwon_UMD = map_loadData()

    # 강원_UMD와 강원_code를 병합한 데이터프레임 생성
    gangwon_sample = pd.merge(gangwon_UMD, gangwon_code, on="EMD_CD")

    visual_feature = forestfire_occurs[["ar", "amount", "latitude", "longitude", "w_regions"]].groupby(
        ["w_regions"]).agg({
        "ar": lambda x: x.astype(float).sum(),
        "amount": lambda x: x.astype(float).sum(),
        "latitude": "mean",
        "longitude": "mean"
    }).reset_index()

    w_regions = {
        'Region': ['강원북부내륙', '강원중부내륙', '강원남부내륙', '강원북부산지', '강원중부산지', '강원남부산지', '강원북부해안', '강원중부해안', '강원남부해안'],
        'Geometry': [
            gangwon_sample[
                (gangwon_sample["address"].str.contains("철원군")) | (gangwon_sample["address"].str.contains("화천군"))][
                'geometry'].unary_union,
            gangwon_sample[(gangwon_sample["address"].str.contains("춘천시")) | (
                        gangwon_sample["address"].str.contains("홍천군") & ~gangwon_sample["address"].str.contains("내면"))][
                'geometry'].unary_union,
            gangwon_sample[
                (gangwon_sample["address"].str.contains("원주시")) | (gangwon_sample["address"].str.contains("횡성군"))][
                'geometry'].unary_union,
            gangwon_sample[
                (gangwon_sample["address"].str.contains("양구군")) | (gangwon_sample["address"].str.contains("인제군"))][
                'geometry'].unary_union,
            gangwon_sample[
                (gangwon_sample["address"].str.contains("홍천군") & gangwon_sample["address"].str.contains("내면")) | (
                            gangwon_sample["address"].str.contains("평창군") & gangwon_sample["address"].str.contains(
                        "대관령면")) | (
                            gangwon_sample["address"].str.contains("평창군") & gangwon_sample["address"].str.contains(
                        "진부면"))]['geometry'].unary_union,
            gangwon_sample[
                (gangwon_sample["address"].str.contains("영월군")) | (gangwon_sample["address"].str.contains("정선군")) | (
                            gangwon_sample["address"].str.contains("평창군") & ~gangwon_sample["address"].str.contains(
                        "대관령면") & ~gangwon_sample["address"].str.contains("진부면"))]['geometry'].unary_union,
            gangwon_sample[
                (gangwon_sample["address"].str.contains("고성군")) | (gangwon_sample["address"].str.contains("속초시")) | (
                    gangwon_sample["address"].str.contains("양양군"))]['geometry'].unary_union,
            gangwon_sample[gangwon_sample["address"].str.contains("강릉시")]['geometry'].unary_union,
            gangwon_sample[
                (gangwon_sample["address"].str.contains("동해시")) | (gangwon_sample["address"].str.contains("삼척시")) | (
                    gangwon_sample["address"].str.contains("태백시"))]['geometry'].unary_union
        ]
    }

    gdf = gpd.GeoDataFrame(w_regions, geometry='Geometry')

    # w_regions별 value_counts 계산
    region_counts = forestfire_occurs['w_regions'].value_counts().reset_index()
    region_counts.columns = ['w_regions', 'Counts']

    # 데이터프레임 생성
    region_counts_df = pd.DataFrame(region_counts)

    # 데이터프레임 생성
    FireCounts = pd.DataFrame({'Region': region_counts_df['w_regions'],
                               'Fire_Counts': region_counts_df['Counts']})

    merged_Count = gdf.merge(FireCounts, on='Region', how='left')

    merged_Count.crs = "EPSG:4326"

    # 지도 생성
    map = folium.Map(location=[37.5, 128], zoom_start=7)

    # GeoDataFrame 생성
    Count_gdf = gpd.GeoDataFrame(merged_Count, geometry='Geometry')

    # 테두리 선 스타일 함수
    def style_function(feature):
        return {
            'fillColor': 'YlOrRd',
            'fillOpacity': 0.7,
            'color': 'black',  # 테두리 선 색상
            'weight': 1,  # 테두리 선 두께
            'dashArray': '5, 5'  # 테두리 선 스타일
        }

    # Choropleth 맵 생성
    folium.Choropleth(
        geo_data=Count_gdf,
        data=Count_gdf,
        columns=['Region', 'Fire_Counts'],
        key_on='feature.properties.Region',
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=0.4,
        line_color='black',  # 폴리곤 테두리 선 색상
        line_weight=3,  # 폴리곤 테두리 선 두께
        line_dash='5, 5',  # 폴리곤 테두리 선 스타일
        legend_name='Fire Counts',
        highlight=True,
        highlight_function=lambda x: {'weight': 3}  # 하이라이트 스타일
    ).add_to(map)

    # 지도 출력
    st_folium(map)


if __name__ == "__main__":
    run_map()