import streamlit as st
from pathlib import Path

import seaborn as sns
import matplotlib.pyplot as plt
from google.cloud import bigquery
from utils import credentials
from eda.Temp import temp_chart
from eda.map import run_map
from data.map_data import map_loadData

import folium

def run_chart1():
    temp_chart()
def run_chart2():
    run_map()
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
def run_chart4():
    pass

def run_eda():
    st.sidebar.markdown("## Exploration for Data")
    eda = st.sidebar.radio('submenu',['Temperature by region', 'Damage Map', 'Chart3', 'Chart4'], label_visibility='collapsed')
    if eda == 'Temperature by region':
        st.markdown("## Temperature by region")
        run_chart1()
    elif eda == 'Damage Map':
        st.markdown("## Damage Map")
        run_chart2()
    elif eda == 'Chart3':
        st.markdown("## Chart3")
        st.warning("please EDA")
        run_chart3()
    elif eda == 'Chart4':
        st.markdown("## Chart4")
        st.warning("please EDA")
        run_chart4()