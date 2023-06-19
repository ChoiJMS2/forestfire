# -*- coding: utf-8 -*-
import streamlit as st
from pathlib import Path

import seaborn as sns
import matplotlib.pyplot as plt
from google.cloud import bigquery
from utils import credentials
from eda.Temp import temp_chart
from eda.map import run_map
from data.map_data import map_loadData
from eda.humidity import run_humidity
from eda.weather import weather_chart

import folium

def run_chart3():
    forestfire_occurs, weather_stations, gangwon_code, gangwon_UMD = map_loadData()
    st.subheader("forestfire_occurs")
    st.dataframe(forestfire_occurs)
    st.subheader("weather_stations")
    st.dataframe(weather_stations)
    st.subheader("gangwon_code")
    st.dataframe(gangwon_code)
    st.subheader("gangwon_UMD")
    st.dataframe(gangwon_UMD)

def run_eda():
    st.sidebar.markdown("## Exploration for Data")
    eda = st.sidebar.radio('submenu',['Temperature by region', 'Damage Map', 'Weather data by region', 'Humidity by region'], label_visibility='collapsed')
    if eda == 'Temperature by region':
        st.markdown("## Temperature by region")
        temp_chart()
    elif eda == 'Damage Map':
        st.markdown("## Damage Map")
        run_map()
    elif eda == 'Weather data by region':
        st.markdown("## Weather data by region")
        weather_chart()
    elif eda == 'Humidity by region':
        st.markdown("## Humidity by region")
        run_humidity()

if __name__ == '__main__':
    run_eda()