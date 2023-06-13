import streamlit as st
from pathlib import Path

import seaborn as sns
import matplotlib.pyplot as plt
from google.cloud import bigquery
from utils import credentials
from eda.Temp import temp_chart

import folium

def run_chart1():
    temp_chart()
def run_chart2():
    pass
def run_chart3():
    pass
def run_chart4():
    pass

def run_eda():
    st.sidebar.markdown("## Exploration for Data")
    eda = st.sidebar.radio('submenu',['Temperature by region', 'Chart2', 'Chart3', 'Chart4'], label_visibility='collapsed')
    if eda == 'Temperature by region':
        st.markdown("## Temperature by region")
        run_chart1()
    elif eda == 'Chart2':
        st.markdown("## Temperature by region")
        run_chart2()
    elif eda == 'Chart3':
        st.markdown("## Chart3")
        st.warning("please EDA")
        run_chart3()
    elif eda == 'Chart4':
        st.markdown("## Chart4")
        st.warning("please EDA")
        run_chart4()