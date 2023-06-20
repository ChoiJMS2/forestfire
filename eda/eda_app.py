# -*- coding: utf-8 -*-
import streamlit as st
from eda.map import run_map
from data.map_data import map_loadData
from eda.weather import weather_chart

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
    eda = st.sidebar.radio('submenu',['Weather data by region', 'Damage Map', 'Chart3', 'Chart4'], label_visibility='collapsed')
    if eda == 'Weather data by region':
        st.markdown("## Weather data by region")
        weather_chart()
    elif eda == 'Damage Map':
        st.markdown("## Damage Map")
        run_map()
    elif eda == 'Chart3':
        st.markdown("## Chart3")
        pass
    elif eda == 'Chart4':
        st.markdown("## Chart4")
        pass

if __name__ == '__main__':
    run_eda()